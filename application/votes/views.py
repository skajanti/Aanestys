from application import app, db
from application.votes.models import Candidate
from application.votes.forms import CandidateForm, VoterForm

from flask import redirect, render_template, request, url_for
from flask_login import login_required

@app.route("/votes", methods=["GET"])
def votes_index():
	return render_template("votes/list.html", votes = Candidate.query.all())

@app.route("/votes/new/")
@login_required
def candidate_form():
	return render_template("votes/new.html", form = CandidateForm())

@app.route("/votes/<candidate_id>/", methods=["POST"])
@login_required
def candidate_set_party(candidate_id):

	p = Candidate.query.get(candidate_id)
	p.party = request.form.get("party")
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes/", methods=["POST"])
@login_required
def candidate_create():
	form = CandidateForm(request.form)

	#c = Candidate(request.form.get("name"))

	c = Candidate(form.name.data)
	c.party = form.party.data

	if not form.validate():
		return render_template("votes/new.html", form = form)

	db.session().add(c)
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes/<candidate_id>/", methods=["POST"])
@login_required
def candidate_remove(candidate_id):
	c = Candidate.query.get(candidate_id)
	print("debug", c)
	db.session.delete(c)
	db.session.commit()

	#d = addresses_table.delete(Candidate.query.get(id))
	#d.execute()

	return redirect(url_for("votes_index"))

@app.route("/votes/new_voter/")
@login_required
def voter_form():
	return render_template("votes/new_voter.html", form = VoterForm)()

@app.route("/votes/", methods=["POST"])
@login_required
def voter_create():
	form = VoterForm(request.form)

	v = Voter(form.name.data)

	if not form.validate():
		return render_template("votes/new_voter.html", form = form)()

	db.session().add(v)
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes/", methods=["GET"])
def voter_index():
	return render_template("votes/voter_list.html", votes = Voter.query.all())