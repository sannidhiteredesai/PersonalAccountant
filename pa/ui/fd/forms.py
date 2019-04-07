from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from pa.pa.bank import Banks

banks = Banks()


def FDForm(current_user):
    class FDFormContents(FlaskForm):
        fd_bank = SelectField('Bank Name',
                              choices=[('', 'Select')] +
                                      [(b['bank_name'], b['bank_name']) for b in
                                       banks.get_all_bank_branch_names(current_user.username)],
                              validators=[DataRequired()])
        # bank_branch = None  # Select Field
        # first_name = None  # Select Field
        # joint_name = None  # Select Field
        # mode = None  # RadioField
        # type = None  # RadioField
        # interest_account = None  # StringField
        # fd_number = None  # StringField
        # start_date = None  # DateField
        # end_date = None  # DateField
        # days = None  # StringField
        # roi = None  # FloatField
        # princpal_amount = None  # FloatField
        # maturity_amount = None  # FloatField
        add_bank = SubmitField('Add FD')

    return FDFormContents()
