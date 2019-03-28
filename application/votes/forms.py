from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CandidateForm(FlaskForm):
    name = StringField("Candidate name", [validators.Length(min=2)])
    party = StringField("Candidate party", [validators.Length(min=2)])

    class Meta:
        csrf = False


class VoterForm(FlaskForm):
    name = StringField("Voter name", [validators.Length(min=2)])
 
    class Meta:
        csrf = False