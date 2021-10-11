from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange

DEFAULT_PIC = "https://tinyurl.com/demo-cupcake"

class AddCupcakeForm(FlaskForm):
    """Form to add a new cupcake"""
    flavor = StringField("Flavor", validators=[InputRequired(message="Flavor can't be blank")])
    size = RadioField("Size", choices=[("small", "small"), ("medium", "medium"), ("large", "large")])
    rating = FloatField("rating", validators=[NumberRange(min=0, max=10, message="rating can't be blank")])
    image = StringField("Image URL", validators=[Optional(), URL()], default=DEFAULT_PIC)