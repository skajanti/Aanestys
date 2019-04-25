from application import db

class Vote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
	voter_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
	year = db.Column(db.Integer)

	def __init__(self, candidate_id, voter_id):
		self.year = 0
		self.candidate_id = candidate_id
		self.voter_id = voter_id
