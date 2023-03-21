from Level2.chat_room.flask_app import app
from Level2.chat_room.flask_app.routes import socketio

if __name__ == "__main__":
    socketio.run(app, host='192.168.1.232', port=80, debug=True)
