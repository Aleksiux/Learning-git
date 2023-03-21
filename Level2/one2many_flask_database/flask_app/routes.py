from flask import render_template, redirect, url_for
from Level2.one2many_flask_database.flask_app.forms import ChildForm, ParentForm
from Level2.one2many_flask_database.flask_app.models import Child, Parent
from Level2.one2many_flask_database.flask_app import db, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/child')
def children():
    try:
        children = Child.query.all()
    except:
        children = []
    return render_template('children.html', children=children)


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
        if form.parents.data:
            child = Child(name=form.name.data,
                          surname=form.surname.data,
                          age=form.age.data,
                          parent_id=form.parents.data.id)
        else:
            child = Child(name=form.name.data,
                          surname=form.surname.data,
                          age=form.age.data)
        db.session.add(child)
        db.session.commit()
        return redirect(url_for('children'))

    return render_template('add_child.html', form=form)


@app.route('/add_parent', methods=['GET', 'POST'])
def add_parent():
    form = ParentForm()
    if form.validate_on_submit():
        parent = Parent(name=form.name.data,
                        surname=form.surname.data,
                        age=form.age.data)
        for child in form.children.data:
            new_child = Child.query.get(child.id)
            parent.children.append(new_child)
        db.session.add(parent)
        db.session.commit()
        return redirect(url_for('parents'))
    return render_template('add_parent.html', form=form)
