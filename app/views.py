from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from .forms import LocationForm
from .models import Location
from config import LOCATIONS_PER_PAGE

@app.route('/', methods=['Get', 'Post'])
@app.route('/index', methods=['Get', 'Post'])
@app.route('/index/<int:page>', methods=['Get', 'Post'])
def index(page=1):
	locations = Location.query.order_by(Location.name).paginate(page,LOCATIONS_PER_PAGE, False)
	return render_template('index.html',locations=locations)

@app.route('/add_location',methods=['Get', 'Post'])
def add_location():
	form = LocationForm()
	if form.validate_on_submit():
		location = Location.query.filter_by(device_id=form.device_id.data).first()
		if location is None:
			location = Location(device_id=form.device_id.data, name=form.name.data, address=form.address.data, occupancy_count=0)
			db.session.add(location)
			db.session.commit()
		return redirect(url_for('index'))
	return render_template('add_location.html',title='Add Location',form=form)