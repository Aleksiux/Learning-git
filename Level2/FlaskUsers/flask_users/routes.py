from Level2.FlaskUsers.flask_users import app, db, bcrypt, login_manager
from Level2.FlaskUsers.flask_users.forms import RegisterForm, LoginForm, UserUpdateForm, ChangePasswordForm, \
    RequestChangePasswordForm, UserForm, MessagesForm
from flask import render_template, redirect, url_for, flash, abort, session, request
from Level2.FlaskUsers.flask_users.models import Users
from flask_login import login_required, logout_user, login_user, current_user
from Level2.FlaskUsers.flask_users.utils import save_picture, send_reset_email, generate_unique_code, rooms
from flask_socketio import join_room, leave_room, send, SocketIO


socketio = SocketIO(app)


@login_manager.user_loader
def load_user(user_id: int):
    return Users.query.get(int(user_id))  # Taking users object


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data,
                     first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     email=form.email.data,
                     password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('Registration complete!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = Users.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Logged in successfully !', 'success')
                return redirect(url_for('account'))
            else:
                flash('Login failed! Check email or password', 'danger')
        except Exception as e:
            print(e)
            abort(500)
    return render_template('login.html', form=form)


@app.route('/account')
@login_required
def account():
    photo = url_for('static', filename='profile_pictures/' + current_user.photo)
    return render_template('account.html', photo=photo)


@app.route('/update_account', methods=['GET', 'POST'])
@login_required
def update_account():
    form = UserUpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        if form.photo.data:
            current_user.photo = save_picture(form.photo.data)
        db.session.commit()
        flash('Updated successfully !', 'success')
        return redirect(url_for('account'))
    photo = url_for('static', filename='profile_pictures/' + current_user.photo)
    return render_template('update_account.html', form=form, photo=photo)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('index'))
    form = RequestChangePasswordForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Check your email for more info', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = Users.verify_reset_token(token)
    if user is None:
        # TODO: check if link was used.
        flash('Request is invalid or link is expired', 'warning')
        return redirect(url_for('reset_request'))
    form = ChangePasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password was updated, you can login now :)', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', title='Reset Password', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/chat_room', methods=['GET', 'POST'])
def chat_room():
    form = UserForm()
    session.clear()
    if request.method == 'POST':
        name = request.form.get('name')
        room_code = request.form.get('room_code')
        submit_join = request.form.get('submit_join', False)
        submit_create = request.form.get('submit_create', False)

        if submit_join and not room_code:
            return render_template('chat_room.html', error='Please enter room code if you trying to join.',
                                   name=name, room_code=room_code, form=form)

        room = room_code
        if submit_create:
            room = generate_unique_code(4)
            rooms[room] = {'members': 0, 'messages': []}
        elif room_code not in rooms:
            return render_template('chat_room.html', error='Room does not exist. Check code again.', name=name,
                                   room_code=room_code, form=form)
        session['room'] = room
        session['name'] = name
        return redirect(url_for('room'))

    return render_template('chat_room.html', form=form)


@app.route('/room')
def room():
    form = MessagesForm()
    room = session.get('room')
    if room is None or session.get('name') is None or room not in rooms:
        return redirect(url_for('home'))
    return render_template('room.html', form=form, code=room, messages=rooms[room]['messages'])


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")


@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return

    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")


@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


@app.route('/raise_404')
def raise_404():
    abort(404)


@app.route('/raise_403')
def raise_403():
    abort(403)


@app.route('/raise_500')
def raise_500():
    abort(500)


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404


@app.errorhandler(403)
def error_403(error):
    return render_template("403.html"), 403


@app.errorhandler(500)
def error_500(error):
    return render_template("500.html"), 500
