from Level2.rest_api.simple_restapi.simple_restapi.simple_restapi import db


# DB objektas
class Uzduotis(db.Model):
    __tablename__ = 'uzduotis'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    atlikta = db.Column("Atlikta", db.Boolean)

    def to_dictionary(self):
        return {"id": self.id, "pavadinimas": self.pavadinimas, "atlikta": self.atlikta}
