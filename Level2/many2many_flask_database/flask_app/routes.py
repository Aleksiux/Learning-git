from flask import render_template, redirect, url_for
from Level2.many2many_flask_database.flask_app.forms import ChildForm, ParentForm
from Level2.many2many_flask_database.flask_app.models import Child, Parent
from Level2.many2many_flask_database.flask_app import db, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/children')
def children():
    try:
        children = Child.query.all()
    except:
        children = []
    return render_template('children.html', children=children)


@app.route('/parents')
def parents():
    try:
        parents = Parent.query.all()
    except:
        parents = []
    return render_template('parent.html', parents=parents)


@app.route('/add_children', methods=['GET', 'POST'])
def add_children():
    form = ChildForm()
    if form.validate_on_submit():
        child = Child(name=form.name.data,
                      surname=form.surname.data,
                      age=form.age.data)
        for parent in form.parents.data:
            new_parent = Parent.query.get(parent.id)
            child.parents.append(new_parent)
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


@app.route('/delete_parent/<int:id>', methods=['GET', 'POST'])
def delete_parent(id):
    deleted_parent = Parent.query.get(id)
    db.session.delete(deleted_parent)
    db.session.commit()
    return redirect(url_for('parents'))


@app.route('/delete_child/<int:id>', methods=['GET', 'POST'])
def delete_child(id):
    deleted_child = Child.query.get(id)
    db.session.delete(deleted_child)
    db.session.commit()
    return redirect(url_for('children'))


@app.route('/update_parent/<int:id>', methods=['GET', 'POST'])
def update_parent(id):
    updated_parent = Parent.query.get(id)
    form = ParentForm()
    if form.validate_on_submit():
        updated_parent.name = form.name.data
        updated_parent.surname = form.surname.data
        updated_parent.age = form.age.data
        updated_parent.children = []
        for child in form.children.data:
            new_child = Child.query.get(child.id)
            updated_parent.children.append(new_child)
        db.session.commit()
        return redirect((url_for('parents')))
    return render_template('update_parent.html', form=form, parent=updated_parent)


@app.route('/update_child/<int:id>', methods=['GET', 'POST'])
def update_child(id):
    updated_child = Child.query.get(id)
    form = ChildForm()
    if form.validate_on_submit():
        updated_child.name = form.name.data
        updated_child.surname = form.surname.data
        updated_child.age = form.age.data
        updated_child.parent = []
        for parent in form.parents.data:
            new_parent = Parent.query.get(parent.id)
            updated_child.children.append(new_parent)
        db.session.commit()
        return redirect((url_for('children')))
    return render_template('update_child.html', form=form, child=updated_child)
