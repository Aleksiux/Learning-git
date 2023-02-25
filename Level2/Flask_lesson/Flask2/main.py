from flask import Flask, render_template, request
from dictionary import data
from forms import ContactForm, RegistrationForm, Yt_Downloader
from yt_downloader import Download
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def main():
    return render_template('income_form.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/articles")
def articles():
    return render_template('articles.html', data=data)


@app.route('/<string:title>')
def article(title):  # < -- kintamasis is html
    return render_template('article.html', article_name=title, data=data)  # priskiriu title prie naujo kintamojo


@app.route("/articles_by_id")
def articles_by_id():
    return render_template('articles_by_id.html', data=data)


@app.route('/<int:id>/<string:date>')
def article_by_id(id, date):  # < -- kintamasis is html
    return render_template('article_by_id.html', id_unique=id, date=date, data=data)


@app.route('/add_article')
def add_article():
    return render_template('add_article.html')


@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('contact_success.html', form=form)
    return render_template('contact_us.html', form=form)


@app.route('/registration_form', methods=['GET', 'POST'])
def registration_form():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template('registration_success.html', form=form)
    return render_template('registration_form.html', form=form)


@app.route('/yt_downloader', methods=['GET', 'POST'])
def yt_downloader():
    form = Yt_Downloader()
    if form.validate_on_submit():
        Download(form.downloader.data)
        return render_template('yt_downloader.html', form=form)
    return render_template('yt_downloader.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        author = request.form['author']
        text = request.form['text']
        name = request.form['name']
        data.append({
            # 'id': max([int(d['id']) for d in data]) + 1,
            'date': date,
            'author': author,
            'name': name,
            'text': text,
            'status': 'published'
        })
    return render_template('articles.html', data=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
