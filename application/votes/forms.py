from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CandidateForm(FlaskForm):
    name = StringField("Candidate name", [validators.Length(min=2)])
    party = StringField("Candidate party")
 
    class Meta:
        csrf = False