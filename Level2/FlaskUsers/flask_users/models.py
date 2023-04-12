from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from Level2.FlaskUsers.flask_users import db
from flask_login import UserMixin
from Level2.FlaskUsers.flask_users import app


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(50), unique=True, nullable=False)
    first_name = db.Column('first_name', db.String(80), nullable=False)
    last_name = db.Column('last_name', db.String(80), nullable=False)
    photo = db.Column(db.String(20), nullable=False, default='default.png')
    email = db.Column('email', db.String(80), unique=True, nullable=False)
    password = db.Column('password', db.String(100), nullable=False)
    privilege = db.Column('privilege', db.Integer, default=0, nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)
