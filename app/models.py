from app import db

class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True) #Default id, allows for easier changing of devices if needed.
	device_id = db.Column(db.String(24), index=True, unique=True) #Keeps track of which spark core is being used at this location.
	name = db.Column(db.String(64), index=True) #The human readable name of the location
	address = db.Column(db.String(80), index=True, unique=True) #The human readable address of the location.
	#latitude = db.Column(db.Float, index=True, unique=True) #Store the gps coordinates of the location.
	#longitude = db.Column(db.Float, index=True, unique=True)
	occupancy_count = db.Column(db.Integer, index=True) #Stores the current estimate of how many people are at this location.
	#last_updated = db.Column(db.DateTime) #Stores when the occupancy_count for this location was last updated.

	def __repr__(self):
		return '<Location: %r>' % (self.name)




