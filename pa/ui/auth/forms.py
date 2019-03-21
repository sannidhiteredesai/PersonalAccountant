import enum
from pa.pa.user import Users
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class Validations:
    @staticmethod
    def is_valid_mobile(number):
        if not number: return False

        def is_int(input_):
            try:
                int(input_)
                return True
            except ValueError:
                return False

        return len(number) == 10 and is_int(number)

    @staticmethod
    def mobile_already_exists(number):
        return Users().exists_mobile(number)

    @staticmethod
    def user_already_exists(username):
        return Users().exists(username)


class SecretQuestions(enum.Enum):
    BIRTH_PLACE = 'What was your birth place ?'
    SCHOOL_NAME = 'What was your school name ?'
    COLLEGE_NAME = 'What was your college name ?'

    @staticmethod
    def get_questions():
        questions = []
        for question in SecretQuestions:
            questions.append((question.name, question.value))
        return questions


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    mobile = StringField('Mobile number', validators=[DataRequired()])
    dob = DateField('Date of birth [ dd/mm/yyyy ]',
                    format='%d/%m/%Y',
                    validators=[DataRequired(message='Please provide a valid date in dd/mm/yyyy format.')])

    question = SelectField('Secret Question',
                           choices=[('', 'Please select an option')] + SecretQuestions.get_questions(),
                           validators=[DataRequired()])
    answer = StringField('Answer to Secret Question', validators=[DataRequired()])

    submit = SubmitField('Submit')

    def validate_username(self, username):
        if Validations.user_already_exists(username.data):  # Validate username is unique
            raise ValidationError('Please use a different username.')

    def validate_mobile(self, mobile):
        if not Validations.is_valid_mobile(mobile.data):  # Validate mobile number is 10 digit
            raise ValidationError('Please give a 10 digit mobile number.')

        if Validations.mobile_already_exists(mobile.data):  # Validate mobile number is unique
            raise ValidationError('Please use a different mobile number.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
