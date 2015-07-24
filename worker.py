from app import models, db
from config import ACCESS_TOKEN, SPARK_OCCUPANCY
import requests, sched, time


s = sched.scheduler(time.time, time.sleep)

def repeated_code(sc):
	locations = models.Location.query.all()

	#Set up the spark api compliant post ? parameters
	payload = {'access_token': ACCESS_TOKEN}

	for l in locations:
		url = 'https://api.particle.io/v1/devices/' + l.device_id #  + '/' + SPARK_OCCUPANCY
		print url
		r = requests.get(url,params=payload)
		print r
		#Update the occupancy count stored in the database based on the value read in from spark core.
		if r.status_code == requests.codes.ok:
			js = r.json()
			print js
			if js['result'] is not None:
				l.occupancy_count = js['result']
				db.session.commit()
	sc.enter(2,1,repeated_code, (sc,))

s.enter(2,1,repeated_code,(s,))
s.run()
