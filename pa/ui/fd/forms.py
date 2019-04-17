from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, DateField, FloatField
from wtforms.validators import DataRequired


def FDForm(banks, members):
    class FDFormContents(FlaskForm):
        bank_name = SelectField('Bank Name',
                                choices=[('', 'Select')] + [(b, b) for b in banks],
                                validators=[DataRequired()])

        bank_branch = SelectField('Bank Branch',
                                  choices=[('', 'Select')] + [(branch, branch) for branches in banks.values()
                                                              for branch in branches],
                                  validators=[DataRequired()])

        first_name = SelectField('First Name',
                                 choices=[('', 'Select')] + [(m, m) for m in members],
                                 validators=[DataRequired()])

        joint_name = SelectField('Joint Name',
                                 choices=[('', 'Select')] + [(m, m) for m in members])

        mode = SelectField('Mode of Operation',
                           choices=[('Ei/Sur', 'Ei/Sur'), ('Single', 'Single')],
                           validators=[DataRequired()])

        type = SelectField('Type',
                           choices=[('Cumulative', 'Cumulative'), ('Quarterly', 'Quarterly')],
                           validators=[DataRequired()])

        interest_account = StringField('Interest Credited In Account')

        fd_number = StringField('FD Number', validators=[DataRequired()])

        start_date = DateField('Start Date [ dd/mm/yyyy ]',
                               format='%d/%m/%Y',
                               validators=[DataRequired(message='Please provide a valid date in dd/mm/yyyy format.')])

        end_date = DateField('Maturity Date [ dd/mm/yyyy ]',
                             format='%d/%m/%Y',
                             validators=[DataRequired(message='Please provide a valid date in dd/mm/yyyy format.')])

        period = StringField('Period', validators=[DataRequired()])

        roi = FloatField('Rate of Interest', validators=[DataRequired()])

        principal_amount = FloatField('Principal Amount', validators=[DataRequired()])

        maturity_amount = FloatField('Maturity Amount', validators=[DataRequired()])

        add_bank = SubmitField('Add FD')

    return FDFormContents()
