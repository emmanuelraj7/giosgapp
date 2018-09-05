"""To run the app, execute the command "python server.py start" and then
open a browser and go to http://localhost:5000/
"""
import flask_script
import connecttoapi

MANAGER = flask_script.Manager(connecttoapi.app)
MANAGER.add_command('start', flask_script.Server(host='localhost'))
MANAGER.run()
