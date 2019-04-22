from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CandidateForm(FlaskForm):
    name = StringField("Candidate name", [validators.Length(min=2)])
    party = StringField("Candidate party", [validators.Length(min=2)])

    class Meta:
        csrf = False

class SetPartyForm(FlaskForm):
    party = StringField("Candidate party", [validators.Length(min=2)])

    class Meta:
        csrf = False