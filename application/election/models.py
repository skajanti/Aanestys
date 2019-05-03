from application import db


class Election(db.Model):
    year = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False)

    vote = db.relationship("Vote", backref='election', lazy=True)

    def __init__(self, year, active):
        self.year = year
        self.active = active
