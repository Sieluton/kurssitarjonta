from application import db
from application.models import Base


class Course(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.TEXT)
    reservations = db.Column(db.Integer, nullable=False, default=0)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
