from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class AddBankBranchForm(FlaskForm):
    bank_name = StringField('Bank Name', validators=[DataRequired()])
    bank_branch = StringField('Bank Branch', validators=[DataRequired()])
    branch_address = TextAreaField('Branch Address', validators=[DataRequired()])
    timings = StringField('Timings', validators=[DataRequired()])
    add_bank = SubmitField('Add Branch')

    def validate_bank_name(self, bank_name):
        raise ValidationError("Use something else !!")