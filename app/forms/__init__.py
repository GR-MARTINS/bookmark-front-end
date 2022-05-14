from wtforms import (
    StringField,
    EmailField,
    PasswordField,
    SubmitField,
    BooleanField,
    SearchField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo
)
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired()]
    )

    email = EmailField(
        "Email", validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password", validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password", validators=[DataRequired()]
    )
    remember = BooleanField("Remember-me")


class CreateBookmarkForm(FlaskForm):
    url = StringField("URL", validators=[DataRequired()])
    body = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("Save")


class SearchBookmarkForm(FlaskForm):
    search = StringField("Search Bookmark", validators=[DataRequired()])
    submit = SubmitField("Search")
