# krowdscout

Running the web-app locally
----------------------------
1.  Setting up the virtual environment:
	
	If you are using Mac OS X, type the following:
	$ sudo easy_install virtualenv
	If you are on linux, such as Ubuntu, type the following:
	$ sudo apt-get install python-virtualenv

	Now we need to construct our virtualenv.  Navigate to the top level 
	directory of the repository and type the following:
	$ virtualenv venv

	To activate our new virtual environment type:
	$ source venv/bin/activate

	Now we need to install our application dependencies in our virtual
	environment, this can be accomplished with the following command:
	$ pip install Flask gunicorn flask-login flask-sqlalchemy sqlalchemy-migrate

2.  Modifying configuration variables:
	
	It is currently assumed that all Spark cores will have the same access token
	and so the ACCESS_TOKEN is stored in the file config.py.  You can find your
	access token by going to the Spark online IDE and clicking on the Settings
	wheel in the bottom left corner.  Update this variable in your config file.

3.  Creating a local database to use:

	You must also create a local database file to use.  Do this by typing the
	following from the top level directory:
	$ ./db_create.py

4.  Running the web-app:
	
	In order to run the web-app we type:
	$ foreman start
	Currently, we most also run the worker script to update spark variables.
	Make sure that you execute this command from within your virtual env.
	$ python worker.py

	If you open your browser and navigate to "localhost:5000" you should now see
	the webpage.

5.  Adding your location/core:
	
	At this point you can add your core to the database by going to the
	"Add Location" link in the top bar of the webpage.  You can find the id of 
	the core that you want to add by going to the Spark online IDE and clicking
	on the device target in the left panel and then selecting your core in the
	pop-up.
