from application import db
from application.models import Base
from application.reservations.models import Reservation
from sqlalchemy.sql import text


class Course(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.TEXT)
    accounts = db.relationship("User", secondary="reservations")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def find_course_reservation_total(course_id):
        stmt = text("SELECT COUNT(course_id)"
                    " FROM reservations"
                    " WHERE course_id = :course_id").params(course_id=course_id)
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]

        return result

    @staticmethod
    def course_reservation_list(course_id):
        stmt = text("SELECT account.name, account.id FROM account "
                    "INNER JOIN reservations ON reservations.account_id = account.id "
                    "WHERE reservations.course_id = :course_id GROUP BY account.name, account.id").params(course_id=course_id)
        res = db.engine.execute(stmt)

        result = []
        for row in res:
            result.append({"name":row[0], "id":row[1]})

        return result

    @staticmethod
    def user_already_in_course(course_id, user_id):
        if Reservation.query.filter_by(course_id=course_id, account_id=user_id).count() > 0:
            return True
