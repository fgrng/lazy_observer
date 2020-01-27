from flask_wtf import FlaskForm
from app.models import Dimension, Subdimension, Indicator

## Import classes that represent the required field types.
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField

## Import classes that represent attached validation behavior.
from wtforms.validators import DataRequired

## ===================================================
## Create Class for each form used in the application.

class RequestSheetForm(FlaskForm):
    subd_choices = [(s.id, s.name) for s in Subdimension.query.order_by('dimension_id')]
    subd_1 = SelectField('Erster Aspekt', choices = subd_choices)
    subd_2 = SelectField('Zweiter Aspekt', choices = subd_choices)
    random = BooleanField('Zufallgenerator?')
    submit = SubmitField('Protokoll erstellen')

class CreateIndicatorForm(FlaskForm):
    subd_choices = [(s.id, s.name) for s in Subdimension.query.order_by('dimension_id')]
    subd = SelectField('Zugehoeriger Aspekt', choices = subd_choices, coerce=int)
    criteria = TextAreaField('Kriteriumsbeschreibung', validators=[DataRequired()])
    submit = SubmitField('Indikator anlegen')

class CreateSubdimensionForm(FlaskForm):
    dim_choices = [(s.id, s.name) for s in Dimension.query.all()]
    dim = SelectField('Zugehoerige Basisdimension', choices = dim_choices, coerce=int)
    name = StringField('Aspekt', validators=[DataRequired()])
    submit = SubmitField('Aspekt anlegen')
