from application import app, db, login_required
from application.votes.models import Candidate, Vote
from application.auth.models import User
from application.votes.forms import CandidateForm, SetPartyForm

from flask import redirect, render_template, request, url_for
from flask_login import current_user
from flask_wtf import FlaskForm
from sqlalchemy.sql.expression import func

@app.route("/votes", methods=["GET"])
def votes_index():
	return render_template("votes/list.html", votes = Candidate.query.all())

@app.route("/votes/new/")
@login_required(role="ADMIN")
def candidate_form():
	return render_template("votes/new.html", form = CandidateForm())

@app.route("/votes/<candidate_id>/", methods=["POST"])
@login_required(role="ADMIN")
def candidate_set_party(candidate_id):
	#form = SetPartyForm(request.form)

	p = Candidate.query.get(candidate_id)
	p.party = request.form.get("party")
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes/", methods=["POST"])
@login_required(role="ADMIN")
def candidate_create():
	form = CandidateForm(request.form)

	c = Candidate(form.name.data)
	c.party = form.party.data

	if not form.validate():
		return render_template("votes/new.html", form = form)

	db.session().add(c)
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes/<candidateid>/remove_candidate", methods=["POST"])
@login_required(role="ADMIN")
def candidate_remove(candidateid):

	print("debug")
	db.session().query(Candidate).filter(Candidate.id == candidateid).delete()

	db.session().commit()
	return redirect(url_for("votes_index"))

@app.route("/votes/<candidate_id>/vote/", methods=["POST"])
@login_required(role="ANY")
def cast_vote(candidate_id):

	v = Vote(candidate_id, current_user.id)

	db.session().add(v)
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes_count", methods=["GET"])
def votes_count():
	return render_template("votes/vote_count.html", votes = Candidate.query.all(), vote_count=Candidate.count_votes())