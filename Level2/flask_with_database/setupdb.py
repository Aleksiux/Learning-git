from app import Message, db, app

app.app_context().push()
db.create_all()

john = Message('john', 'john@mail.com', 'Kažkoks labai rimtas atsiliepimas.', 8558956521)
brown = Message('brown', 'brown@mail.lt', 'Antano nuomonė labai svarbi.', 8558956522)
josh = Message('josh', 'josh@friends.lt', 'Aš labai piktas, nes blogai.', 855895653)
viktor = Message('viktor', 'viktor@yahoo.com', 'Aš tai linksmas esu, man patinka.', 8558956524)

db.session.add_all([john, brown, josh, viktor])
db.session.commit()

