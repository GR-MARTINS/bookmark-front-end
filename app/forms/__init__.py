from wtforms import (
    StringField,
    EmailField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo
)
from flask_wtf import FlaskForm


class Register(FlaskForm):
    username = StringField(
        "Password", validators=[DataRequired()]
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
