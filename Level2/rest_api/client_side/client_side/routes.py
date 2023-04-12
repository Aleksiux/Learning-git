from flask import request, jsonify
from Level2.rest_api.simple_restapi.simple_restapi.simple_restapi import app, db
from Level2.rest_api.simple_restapi.simple_restapi.simple_restapi.models import Uzduotis

# Crud
# @app.route('/uzduotis', methods=['POST'])
# def prideti_uzduoti():
#     db.create_all()
#     pavadinimas = request.json['pavadinimas']
#     atlikta = request.json['atlikta']
#     nauja_uzduotis = Uzduotis(pavadinimas=pavadinimas, atlikta=atlikta)
#     db.session.add(nauja_uzduotis)
#     db.session.commit()
#     return uzduotis_schema.jsonify(nauja_uzduotis)
# #
#
# # cRud
# @app.route('/uzduotis', methods=['GET'])
# def gauti_visas_uzduotis():
# visos_uzduotys = Uzduotis.query.all()
# result = [u.to_json() for u in visos_uzduotys]
# return jsonify(result)


@app.route('/uzduotis', methods=['GET', 'POST'])
def tvarkyti_uzduotis():
    if request.method == 'GET':
        visos_uzduotys = Uzduotis.query.all()
        result = [u.to_dictionary() for u in visos_uzduotys]
        return jsonify(result)
    elif request.method == 'POST':
        db.create_all()
        pavadinimas = request.json['pavadinimas']
        atlikta = request.json['atlikta']
        nauja_uzduotis = Uzduotis(pavadinimas=pavadinimas, atlikta=atlikta)
        db.session.add(nauja_uzduotis)
        db.session.commit()
        return nauja_uzduotis.to_dictionary()

# cRud
@app.route('/uzduotis/<id>', methods=['GET'])
def gauti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    return jsonify(uzduotis.to_dictionary())


# crUd
@app.route('/uzduotis/<id>', methods=['PUT'])
def pakeisti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    uzduotis.pavadinimas = request.json['pavadinimas']
    uzduotis.atlikta = request.json['atlikta']
    db.session.commit()
    return jsonify(uzduotis.to_dictionary())


# cruD
@app.route('/uzduotis/<id>', methods=['DELETE'])
def istrinti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    db.session.delete(uzduotis)
    db.session.commit()
    return jsonify(uzduotis.to_dictionary())
