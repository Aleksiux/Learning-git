from Level2.flask_reminder.flask_app import app,db

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=False)


