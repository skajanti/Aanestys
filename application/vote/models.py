from application import db

class Vote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
	voter_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
	election_year = db.Column(db.Integer, db.ForeignKey("election.year"), nullable=False)

	def __init__(self, candidate_id, voter_id, year):
		self.election_year = year
		self.candidate_id = candidate_id
		self.voter_id = voter_id