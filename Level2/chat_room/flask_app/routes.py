import random
import string

from Level2.chat_room.flask_app import app
from flask import render_template, request, session, redirect, url_for
from Level2.chat_room.flask_app.forms import UserForm, MessagesForm
from flask_socketio import join_room, leave_room, send, SocketIO

rooms = {}

socketio = SocketIO(app)


def generate_unique_code(length):
    while True:
        letters = string.ascii_uppercase
        room_code = ''.join(random.choice(letters) for _ in range(length))
        if room_code not in rooms:
            break
    return room_code


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    session.clear()
    if request.method == 'POST':
        name = request.form.get('name')
        room_code = request.form.get('room_code')
        submit_join = request.form.get('submit_join', False)
        submit_create = request.form.get('submit_create', False)

        if submit_join and not room_code:
            return render_template('home.html', error='Please enter room code if you trying to join.',
                                   name=name, room_code=room_code, form=form)

        room = room_code
        if submit_create:
            room = generate_unique_code(4)
            rooms[room] = {'members': 0, 'messages': []}
        elif room_code not in rooms:
            return render_template('home.html', error='Room does not exist. Check code again.', name=name,
                                   room_code=room_code, form=form)
        session['room'] = room
        session['name'] = name
        return redirect(url_for('room'))

    return render_template('home.html', form=form)


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
