from application import db
from application.models import Base
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
                    " WHERE (course_id) = :course_id").params(course_id=course_id)
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]

        return result
