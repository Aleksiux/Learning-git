from random import randint

from app import db, Message, app

app.app_context().push()

# print all
# all_message = Message.query.all()
# # print(all_message)
#
# print by first id.
# first_message = Message.query.get(1)
# # print(first_message)
#
# filter josh by his name
# name_message = Message.query.filter_by(name='josh')
# print(name_message.all())

# changing josh message
# josh_message = Message.query.get(3)
# josh_message.message = 'New message for josh'
# db.session.add(josh_message)
# db.session.commit()
#
# josh_message_after_adding = Message.query.get(3)

# print(josh_message_after_adding.message)


# adding stasys.
# stasys = Message('Stasys', 'stasys@gmail.com', 'Hello im Stasys')
# db.session.add(stasys)
# db.session.commit()
# stasys = Message.query.get(5)
# print(stasys.message)

#
# stasys = Message.query.get(5)
# db.session.delete(stasys)
# db.session.commit()
# qs = Message.query.all()
# print(qs)

messages = Message.query.all()

for i in messages:
    random_phone = randint(999999, 10000000)
    i.phone = str(random_phone)
    db.session.add(i)

db.session.commit()

for x in messages:
    print(f'{x.id}, {x.name}, {x.email}, {x.phone}, {x.message}')
