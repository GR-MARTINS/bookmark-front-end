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
    BookmarkForm,
    SearchBookmarkForm
)

import requests, json

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
    create_form = BookmarkForm()
    search_form = SearchBookmarkForm()
    if token:
        url = "http://127.0.0.1:5000/api/v1/bookmarks"
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MzIzMTkzOSwianRpIjoiYmZjY2JhOWUtMmE5ZS00MDIwLTllN2ItMWM3MGYxODQ0MzU0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjUzMjMxOTM5LCJleHAiOjE2NTMzMTgzMzl9.7XPUTyrxr-2QYQPDydNBi0vU1MqYp_vJzHB5rLRF6-4"}
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
    form = BookmarkForm()
    response = request.args["response"].replace("'", '"')
    id = json.loads(response)["id"]
    url = f"http://127.0.0.1:5000/api/v1/bookmarks/stats/{id}"
    response = requests.get(url).json()
    return render_template('options.html', data=response, form=form)
