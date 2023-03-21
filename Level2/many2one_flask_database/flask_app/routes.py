from flask import render_template, redirect, url_for
from Level2.many2one_flask_database.flask_app.forms import ChildForm, ParentForm
from Level2.many2one_flask_database.flask_app.models import Child, Parent
from Level2.many2one_flask_database.flask_app import db, app



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/child')
def child():
    try:
        child = Child.query.all()
    except:
        child = []
    return render_template('children.html', children=child)


@app.route('/parent')
def parents():
    try:
        parents = Parent.query.all()
    except:
        parents = []
    return render_template('parent.html', parents=parents)


@app.route('/add_child', methods=['GET', 'POST'])
def add_child():
    db.create_all()
    form = ChildForm()
    if form.validate_on_submit():
        child = Child(name=form.name.data,
                      surname=form.surname.data,
                      age=form.age.data)
        db.session.add(child)
        db.session.commit()
        return redirect(url_for('childs'))
    return render_template('add_child.html', form=form)


@app.route('/add_parent', methods=['GET', 'POST'])
def add_parent():
    form = ParentForm()
    if form.validate_on_submit():
        if form.child.data:
            parent = Parent(name=form.name.data,
                            surname=form.surname.data,
                            age=form.age.data,
                            child_id=form.child.data.id)
        else:
            parent = Parent(name=form.name.data,
                            surname=form.surname.data,
                            age=form.age.data)
        db.session.add(parent)
        db.session.commit()
        return redirect(url_for('parents'))
    return render_template('add_parent.html', form=form)
