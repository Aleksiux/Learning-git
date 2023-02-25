from app import db, app, Gpu

app.app_context().push()
# db.create_all()
query_gpu = Gpu.query.order_by(Gpu.price.asc()).all()



# Person.query.order_by(Person.id.desc()).all()