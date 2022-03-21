from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField,  IntegerField, SubmitField, DecimalField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    
    title = StringField('Title',validators=[DataRequired()])

    numberofbdr = IntegerField('Number of Bedrooms',validators=[DataRequired()])

    numberofbath = IntegerField('Number of Bathrooms',validators=[DataRequired()])
    
    location = StringField('Location',validators=[DataRequired()])
    
    price = DecimalField('Price',validators=[DataRequired()])

    property_type = SelectField('Property Type',choices=[('house', 'House'), ('apartment', 'Apartment')])

    description = TextAreaField('Description',validators=[DataRequired()])

    photo = FileField('Photo', validators=[ FileRequired(),FileAllowed(['jpg', 'png', 'Images only!']) ])

    submit = SubmitField("Add Property")