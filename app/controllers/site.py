from flask import (
    Blueprint,
    render_template
)
from app.forms import Login, Register, Bookmark

site = Blueprint("site", __name__)


@site.route('/')
def index():
    form = Bookmark()
    return render_template("home.html", form=form)


@site.route('/login')
def login():
    form = Login()
    return render_template("login.html", form=form, title="Login")


@site.route('/register')
def register():
    form = Register()
    return render_template("register.html", form=form, title="Register")
