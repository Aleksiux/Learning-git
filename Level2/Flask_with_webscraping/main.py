from flask import render_template, request
import os
from forms import GpuSearch
from gpu_scraper import gpu_scraping
from app import db, app, Gpu
from crud import query_gpu
from weather import return_weather

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
weather = return_weather("kaunas")

@app.route("/")
def main():
    # weather = return_weather("kaunas")
    return render_template('index.html', weather=weather)


@app.route('/pigu_search', methods=['GET', 'POST'])
def pigu_search():
    form = GpuSearch()
    if form.validate_on_submit():
        gpu_name = request.form['gpu_name']
        gpu_dict = gpu_scraping(gpu_name)
        for gpu_dictionary in gpu_dict:
            gpu = Gpu(gpu_dictionary['GPU'], gpu_dictionary['GPU_price'])
            db.session.add(gpu)
            db.session.commit()
        data = query_gpu
        return render_template('pigu_search.html', form=form, data=data, weather=weather)
    data = query_gpu
    return render_template('pigu_search.html', form=form, data=data, weather=weather)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
