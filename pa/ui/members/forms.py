from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from pa.pa.member import Members
from flask_login import current_user

class MemberForm(FlaskForm):
    membername = StringField('Member first name', validators=[DataRequired()])
    submit = SubmitField('Add new member')

    def validate_membername(self, membername):
        if Members().exists(member=membername.data, for_user=current_user.username):  # Validate member name is unique
            raise ValidationError('Member already exists, use a different name.')

