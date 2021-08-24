from flask_wtf import FlaskForm
import wtforms.fields as wtFields
import wtforms.validators as wtValidate


class FormLogin(FlaskForm):
    username = wtFields.StringField('Username', validators=[wtValidate.Length(min=6, max=25), wtValidate.DataRequired()])
    #email = wtFields.PasswordField('Email', validators=[wtValidate.Email(), wtValidate.DataRequired()])
    password = wtFields.PasswordField('Password', validators=[wtValidate.Length(min=4), wtValidate.DataRequired()])
    #password2 = wtFields.PasswordField('Confirm Password', wtValidate=[wtValidate.EqualTo('password), wtValidate.DataRequired()])
    submit = wtFields.SubmitField(label='Entrar')

