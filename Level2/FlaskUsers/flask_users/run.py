from Level2.FlaskUsers.flask_users import app, db
from Level2.FlaskUsers.flask_users.routes import socketio
from flask_socketio import send


def handle_message(message):
    print("Received message: " + message)
    if message != "User connected":
        send(message, broadcast=True)


if __name__ == '__main__':
    db.create_all()
    # app.run(host='127.0.0.1', port=8000, debug=True)
    socketio.run(app, host='192.168.1.232', debug=True)
