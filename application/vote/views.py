from application import app, db, login_required
from application.candidate.models import Candidate
from application.vote.models import Vote
from application.auth.models import User

from flask import redirect, render_template, request, url_for
from flask_login import current_user
from flask_wtf import FlaskForm

@app.route("/candidates/<candidate_id>/vote/", methods=["POST"])
@login_required(role="ANY")
def cast_vote(candidate_id):

	v = Vote(candidate_id, current_user.id)

	db.session().add(v)
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes_count", methods=["GET"])
def votes_count():
	return render_template("vote/vote_count.html", votes = Candidate.query.all(), vote_count=Candidate.count_votes())