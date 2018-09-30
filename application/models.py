from application import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Reservation(Base):
    __tablename__ = 'reservations'
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    account = db.relationship("User", backref=db.backref("reservations", cascade="all, delete-orphan"))
    course = db.relationship("Course", backref=db.backref("reservations", cascade="all, delete-orphan"))
