from flask import (
    Blueprint,
    render_template
)
from app.forms import Login, Register

site = Blueprint("site", __name__)


@site.route('/')
def index():
    return render_template("index.html")


@site.route('/login')
def login():
    form = Login()
    return render_template("login.html", form=form, title="Login")


@site.route('/register')
def register():
    form = Register()
    return render_template("register.html", form=form, title="Register")
