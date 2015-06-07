from flask.ext.wtf import Form 
from wtforms import StringField
from wtforms.validators import DataRequired

class LocationForm(Form):
	name = StringField('name', validators=[DataRequired()])
	device_id = StringField('device_id', validators=[DataRequired()])
	address = StringField('address', validators=[DataRequired()])