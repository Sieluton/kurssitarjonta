from application import db
from application.models import Base


class Reservation(Base):
    __tablename__ = 'reservations'
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    account = db.relationship("User", backref=db.backref("reservations", cascade="all, delete-orphan"))
    course = db.relationship("Course", backref=db.backref("reservations", cascade="all, delete-orphan"))