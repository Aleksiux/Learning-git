from Level2.items_buy_rest_api.simple_restapi.simple_restapi import db


# DB object
class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column("item_name", db.String)
    price = db.Column("price", db.Float)
    quantity = db.Column("quantity", db.Integer)

    def to_dictionary(self):
        return {"id": self.id, "item_name": self.item_name, "price": self.price, "quantity": self.quantity}
