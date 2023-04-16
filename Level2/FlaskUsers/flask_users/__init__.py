import os
from flask import Flask, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_socketio import SocketIO, send

app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'SECRET_KEY125'
app.app_context().push()

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Login to go further'
# TODO: Need to think about how to use sockets for chatting
# socketio = SocketIO(app, cors_allowed_origins='*')


class AuthMixin(object):
    def is_accessible(self):
        return current_user.is_authenticated()

    def _handle_view(self, name, **kwargs):
        try:
            if not current_user.privilege == 1:
                return redirect(url_for("raise_403"))
        except AttributeError:
            return redirect(url_for("raise_403"))


class AdminModelView(AuthMixin, ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.privilege == 1

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('raise_403'))


class AdminIndex(AuthMixin, AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.privilege == 1

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('raise_403'))


from Level2.FlaskUsers.flask_users.models import Users

admin = Admin(app, index_view=AdminIndex())
admin.add_view(AdminModelView(Users, db.session))
admin.add_link(MenuLink(name='Home', url='/', category='Links'))
from Level2.FlaskUsers.flask_users import routes
