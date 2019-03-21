from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MemberForm(FlaskForm):
    member_name = StringField('Member Name', validators=[DataRequired()])