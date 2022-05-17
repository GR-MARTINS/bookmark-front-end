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

@site.route("/<int:page>", methods=["GET", "POST"])
@site.route("/", methods=["GET", "POST"])
def index(page=1):
    token = "a"
    create_form = CreateBookmarkForm()
    search_form = SearchBookmarkForm()
    if token:
        url = "http://127.0.0.1:5000/api/v1/bookmarks"
        headers = {"Authorization": "Bearer "}
        bookmarks = requests.get(
            url,
            headers=headers,
            params={"page": page}).json()
        if create_form.validate_on_submit():
            bookmark = {
                "body": create_form.body.data,
                "url": create_form.url.data
            }
            requests.post(url + "/", headers=headers, json=bookmark)
        if search_form.validate_on_submit():
            ...

        return render_template(
            "index.html",
            create_form=create_form,
            search_form=search_form,
            token=token,
            bookmarks=bookmarks,
            page=page,
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
