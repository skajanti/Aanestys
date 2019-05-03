from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CandidateForm(FlaskForm):
    name = StringField("Candidate name", [validators.Length(min=2, message="Name must be at least 2 characters long.")
        , validators.Length(max=64, message="Name cannot be longer than 64 characters.")])
    party = StringField("Candidate party", [validators.Length(min=2, message="Party must be at least 2 characters long.")
        , validators.Length(max=32, message="Party cannot be longer than 32 characters")])

    class Meta:
        csrf = False

class SetPartyForm(FlaskForm):
    party = StringField("Candidate party", [validators.Length(min=2), validators.Length(max=32)])

    class Meta:
        csrf = False