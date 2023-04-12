from Level2.items_buy_rest_api.client_side.client_side import app
import requests
from Level2.items_buy_rest_api.client_side.client_side.forms import ItemForm
import json
from flask import render_template, redirect, url_for, request


@app.route('/', methods=['GET'])
def index():
    try:
        response = requests.get('http://127.0.0.1:8000/item')
        items = json.loads(response.text)
    except:
        items = []
    return render_template('items.html', items=items)


@app.route('/add_item', methods=['POST', 'GET'])
def get_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = {
            'item_name': form.item_name.data,
            'price': form.price.data,
            'quantity': form.quantity.data
        }
        requests.post('http://127.0.0.1:8000/item', json=item)
        return redirect(url_for('index'))
    return render_template('add_item.html', form=form)


@app.route('/update_item/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    response = requests.get(f'http://127.0.0.1:8000/get_item/{id}')
    form = ItemForm()
    item = json.loads(response.text)
    if request.method == 'POST':
        if form.validate_on_submit():
            updated_item = {
                'item_name': form.item_name.data,
                'price': form.price.data,
                'quantity': form.quantity.data
            }
            requests.post(f'http://127.0.0.1:8000/change_item/{id}', json=updated_item)
            return redirect(url_for('index'))
    return render_template('update_item.html', form=form, item=item)


@app.route('/delete_item/<int:id>', methods=['GET'])
def delete_item(id):
    requests.delete(f'http://127.0.0.1:8000/del_item/{id}')
    return redirect(url_for('index'))
