from flask import Flask, render_template, request
import os
from app import db, Person, app
from forms import MessageForm
from get_meme import get_meme

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=['GET', 'POST'])
def main():
    form = MessageForm()
    if form.validate_on_submit():
        name = request.form['name']
        surname = request.form['surname']
        message = request.form['message']
        person = Person(name, surname, message=message)
        db.session.add(person)
        db.session.commit()
        data = Person.query.order_by(Person.id.desc()).all()  # or Person.query.all()[::-1]
        return render_template('index.html', form=form, data=data)
    data = Person.query.order_by(Person.id.desc()).all()
    return render_template('income_form.html', form=form, data=data)


@app.route("/about")
def about():
    meme_pic, subreddit = get_meme()
    return render_template('about.html', meme_pic=meme_pic, subreddit=subreddit)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
