from application import db

class Candidate(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144))
	party = db.Column(db.String(32))

	def __init__(self, name):
		self.name = name

class Vote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
	voter_id = db.Column(db.Integer, db.ForeignKey("voter.id"), nullable=False)
	year = db.Column(db.Integer)

	def __init__(self, year):
		self.year = 0

class Voter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144))

	def __init__(self, name):
		return self.name