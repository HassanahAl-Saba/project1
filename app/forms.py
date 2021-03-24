from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, TextField, FloatField, FileField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from wtforms.validators import DataRequired

from flask.helpers import send_from_directory

class PropertyForm(FlaskForm):
    title = TextField("Property Title", validators = [DataRequired()])
    bedroom = TextField("Number of Bedrooms", validators = [DataRequired()])
    bathroom = TextField("Number of Bathrooms", validators = [DataRequired()])
    location = TextField("Location", validators = [DataRequired()])
    price = TextField("Price", validators = [DataRequired()])
    type = SelectField("Property Type", choices=[('House', 'House'), ('Apartment', 'Apartment')], validators = [DataRequired()])
    description = TextAreaField("Description", validators =[DataRequired()])
    photo = FileField("Photo", validators = [FileRequired(), FileAllowed(['jpg','png'])])
