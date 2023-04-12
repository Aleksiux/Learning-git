from flask import request, jsonify
from Level2.items_buy_rest_api.simple_restapi.simple_restapi import app, db
from Level2.items_buy_rest_api.simple_restapi.simple_restapi.models import Items


# Crud
@app.route('/item', methods=['POST'])
def add_item():
    print('item post')
    db.create_all()
    item_name = request.json['item_name']
    price = request.json['price']
    quantity = request.json['quantity']
    new_item = Items(item_name=item_name, price=price, quantity=quantity)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dictionary())


# # cRud
@app.route('/item', methods=['GET'])
def get_all_items():
    print('item get')
    all_items = Items.query.all()
    result = [u.to_dictionary() for u in all_items]
    return jsonify(result)


# cRud
@app.route('/get_item/<id>', methods=['GET'])
def get_item(id):
    item = Items.query.get(id)
    return jsonify(item.to_dictionary())


# crUd
@app.route('/change_item/<id>', methods=['PUT', 'POST'])
def change_item(id):
    print('item put')
    item = Items.query.get(id)
    item.item_name = request.json['item_name']
    item.price = request.json['price']
    item.quantity = request.json['quantity']
    db.session.commit()
    return jsonify(item.to_dictionary())


# cruD
@app.route('/del_item/<id>', methods=['DELETE'])
def del_item(id):
    item = Items.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify(item.to_dictionary())
