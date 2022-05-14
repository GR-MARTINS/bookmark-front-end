from flask import (
    Blueprint,
    render_template,
)
from app.forms import (
    LoginForm,
    RegisterForm,
    CreateBookmarkForm
)

site = Blueprint("site", __name__)


@site.route("/")
def index():
    token = "a"
    if token:
        create_form = CreateBookmarkForm()
        return render_template(
            "index.html",
            create_form=create_form,
            token=token
        )

    else:
        return render_template("index.html")


@site.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form, title="Login")


@site.route('/register')
def register():
    form = RegisterForm()
    return render_template("register.html", form=form, title="Register")
