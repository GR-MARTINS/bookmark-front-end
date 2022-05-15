from flask import (
    Blueprint,
    render_template,
    redirect
)
from app.forms import (
    LoginForm,
    RegisterForm,
    CreateBookmarkForm,
    SearchBookmarkForm
)

import requests

site = Blueprint("site", __name__)

@site.route("/<page>")
@site.route("/")
def index(page=1):
    token = "a"
    if token:
        create_form = CreateBookmarkForm()
        search_form = SearchBookmarkForm()
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MjY1MzQwNiwianRpIjoiYmEyNzg4N2MtNTgxMi00NGQ5LWEwMmEtMzAwYjNjYWZkOTQ4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjUyNjUzNDA2LCJleHAiOjI2NTI2NTM0MDV9._Py4wKEWiet0xng1SIKAhMHPcd9h4WCcTyAbJlRd0rM"}
        bookmarks = requests.get(
            "http://127.0.0.1:5000/api/v1/bookmarks",
            headers=headers,
            params={"page": page}).json()

        return render_template(
            "index.html",
            create_form=create_form,
            search_form=search_form,
            token=token,
            bookmarks=bookmarks,
            page=int(page),
            redirect=redirect,
            print=print
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
