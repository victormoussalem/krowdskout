from flask import render_template, flash, redirect, url_for, request, session, jsonify
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

# A route to handle updating locations without a page refresh.
@app.route('/refresh_locations')
def refresh_locations():
	location = Location.query.first()
	return jsonify(result=location.occupancy_count)

# A route to be invoked by the Particle cloud when there is a change in occupancy count.
# Also have access to data, published_at, and event json parameters.  Data is duplicate of occ_change.
@app.route('/update_occupancy', methods=['Post'])
def update_occupancy():
	data = request.get_json(force=True)
	if data is not None:
		device_id = data['coreid']
		if device_id is not None:
			occ_change = data['occ_change']
			if occ_change is not None:
				l = Location.query.filter_by(device_id=device_id).first()
				if l is not None:
					l.occupancy_count= occ_change
					db.session.commit()
					return 'Success!'
	return 'Failure :('
