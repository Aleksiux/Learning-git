from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('income_form.html')


@app.route('/about')
def about():
    data = \
        [{
        'f_name': 'Alex',
        'l_name': 'Kami',
        'password': 'QWERTY'
    },
        {
            'f_name': 'Best',
            'l_name': 'Test',
            'password': 'ZEDSAS'
        },
        {
            'f_name': 'Petras',
            'l_name': 'Petrauskas',
            'password': 'WQEQWRYT'
        }
        ]
    return render_template('about.html', data=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
