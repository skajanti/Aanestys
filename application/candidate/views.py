from application import app, db, login_required
from application.candidate.models import Candidate
from application.vote.models import Vote
from application.auth.models import User
from application.candidate.forms import CandidateForm, SetPartyForm

from flask import redirect, render_template, request, url_for
from flask_login import current_user
from flask_wtf import FlaskForm
from sqlalchemy.sql.expression import func

@app.route("/candidates", methods=["GET"])
def votes_index():
	return render_template("candidate/list.html", votes = Candidate.query.all())

@app.route("/candidates/new/")
@login_required(role="ADMIN")
def candidate_form():
	return render_template("candidate/new.html", form = CandidateForm())

@app.route("/candidates/<candidate_id>/", methods=["POST"])
@login_required(role="ADMIN")
def candidate_set_party(candidate_id):
	#form = SetPartyForm(request.form)

	p = Candidate.query.get(candidate_id)
	p.party = request.form.get("party")
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/candidates/", methods=["POST"])
@login_required(role="ADMIN")
def candidate_create():
	form = CandidateForm(request.form)

	c = Candidate(form.name.data)
	c.party = form.party.data

	if not form.validate():
		return render_template("candidate/new.html", form = form)

	db.session().add(c)
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/candidates/<candidateid>/remove_candidate", methods=["POST"])
@login_required(role="ADMIN")
def candidate_remove(candidateid):

	print("debug")
	db.session().query(Candidate).filter(Candidate.id == candidateid).delete()

	db.session().commit()
	return redirect(url_for("votes_index"))