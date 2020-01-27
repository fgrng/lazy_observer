from app import db
from datetime import datetime

## Model: basic dimensions for teaching quality
class Dimension(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(64), unique=True)

    ## Relation: Dimension has many subdimensions.
    subdimensions = db.relationship('Subdimension', backref='dimension', lazy='dynamic')

    def __repr__(self):
        return '<Dimension {}>'.format(self.name)

## Model: subdimensions for teaching quality
class Subdimension(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(128), unique=True)

    ## Relation: Subdimension belongs to dimension.
    dimension_id = db.Column(db.Integer, db.ForeignKey('dimension.id'))
    ## Relation: Subdimension has many indicatiors.
    indicators = db.relationship('Indicator', backref='subdimension', lazy='dynamic')

    def __repr__(self):
        return '<Subdimension {}>'.format(self.name)

## Model: indicator for teaching quality
class Indicator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    criteria = db.Column(db.String(128), unique=True)

    ## Relation: Indicator belongs to Subdimension.
    subdimension_id = db.Column(db.Integer, db.ForeignKey('subdimension.id'))

    def __repr__(self):
        return '<Indicator {}>'.format(self.criteria)


