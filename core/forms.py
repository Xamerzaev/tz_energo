from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class ResultForm(FlaskForm):
    a = IntegerField("Переменная 'a'", validators=[DataRequired()])
    b = IntegerField("Переменная 'b'", validators=[DataRequired()])
    c = IntegerField("Переменная 'c'", validators=[DataRequired()])
    submit = SubmitField('Начать')   