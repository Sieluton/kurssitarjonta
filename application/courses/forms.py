from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=2)])
    description = TextAreaField("Course description")

    class Meta:
        csrf = False
