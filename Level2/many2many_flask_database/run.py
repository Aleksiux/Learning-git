from Level2.many2many_flask_database.flask_app import app, db

if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
