from application import db
from application.models import Base


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    token = db.Column(db.Integer, default=0)

    courses = db.relationship("Course", secondary="reservations")

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.token == 1:
            return ["ADMIN"]
        return ["ANY"]
