from flask import (
    Blueprint,
    render_template,
    flash,
    request,
    jsonify
)
from app.forms import (
    LoginForm,
    RegisterForm,
    CreateBookmarkForm,
    SearchBookmarkForm
)

import requests

site = Blueprint("site", __name__)


@site.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form, title="Login")


@site.route('/register')
def register():
    form = RegisterForm()
    return render_template("register.html", form=form, title="Register")


@site.route("/<int:page>", methods=["GET", "POST"])
@site.route("/", methods=["GET", "POST"])
def index(page=1):
    token = "a"
    create_form = CreateBookmarkForm()
    search_form = SearchBookmarkForm()
    if token:
        url = "http://127.0.0.1:5000/api/v1/bookmarks"
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MzA0MjY5NywianRpIjoiNTQyODMzZWMtOGYwNy00ZGQ5LWE1NTgtNGI1NTFiMGY4N2FjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjUzMDQyNjk3LCJleHAiOjE2NTMxMjkwOTd9.nRdpYibbS5jabjk2RycDF2sXs-iCgjBDsW0M2bJrzeY"}
        response_get_all = requests.get(
            url,
            headers=headers,
            params={"page": page}
        ).json()
        if create_form.validate_on_submit():
            bookmark = {
                "body": create_form.body.data,
                "url": create_form.url.data
            }
            response = requests.post(url + "/", headers=headers, json=bookmark)
            if response.status_code == 201:
                flash("Bookmark created successfully", "success")
            else:
                flash(response.json()["error"], "info")

        if search_form.validate_on_submit():
            response_get_one = requests.get(
                url + f"/{search_form.search.data}",
                headers=headers
            )
            if search_form.search.data == "0":
                ...

            if response_get_one.status_code == 200:
                return render_template(
                    "index.html",
                    create_form=create_form,
                    search_form=search_form,
                    token=token,
                    response_get_one=response_get_one.json(),
                    page=page
                )

            else:
                flash(response_get_one.json()["message"], 'info')

        return render_template(
            "index.html",
            create_form=create_form,
            search_form=search_form,
            token=token,
            response_get_all=response_get_all,
            page=page,
        )

    else:
        return render_template("index.html")


@site.route('/options', methods=["GET", "POST", "DELETE"])
def options():
    response = request.args
    if response:
        return jsonify(response)
    return render_template('options.html')
