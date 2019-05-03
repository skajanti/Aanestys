from flask_wtf import FlaskForm
from wtforms import IntegerField, validators
from wtforms.validators import NumberRange


class ElectionForm(FlaskForm):
    year = IntegerField("Year", validators=[NumberRange(min=1800, max=2200,
                                                        message="Year must be between 1800 and 2200.")])

    class Meta:
        csrf = False