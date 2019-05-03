from application import app, db, login_required
from application.candidate.models import Candidate
from application.candidate.forms import CandidateForm

from flask import redirect, render_template, request, url_for

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
	db.session().query(Candidate).filter(Candidate.id == candidateid).delete()

	db.session().commit()
	return redirect(url_for("votes_index"))