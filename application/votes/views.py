from application import app, db
from application.votes.models import Candidate
from application.votes.forms import CandidateForm

from flask import redirect, render_template, request, url_for
from flask_login import login_required

@app.route("/votes", methods=["GET"])
def votes_index():
	return render_template("votes/list.html", votes = Candidate.query.all())

@app.route("/votes/new/")
@login_required
def votes_form():
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
	c = Candidate(request.form.get("name"))

    #if not form.validate():
    #    return render_template("votes/new.html", form = form)

	db.session().add(c)
	db.session().commit()

	return redirect(url_for("votes_index"))
