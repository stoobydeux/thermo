from flask import render_template, session, redirect, url_for, jsonify
from . import main
from .. import db

from influxdb import InfluxDBClient

@main.route('/')
def index():
	return render_template('index.html')
	


@main.route('/getPresence')	
def getPresesence():
	return jsonify(
		Presence=1
	)


@main.route('/getLocalWeather')	
def getLocalWeather():




	return jsonify(
		Presence=1
	)

@main.route('/current')		
def currentValues():

	host='localhost'
	port=8086
	user = "root"
	password = "root"
	dbname = "sensors"
	client = InfluxDBClient(host, port, user, password, dbname)
	query = 'show tag values with key = device;'
	print("Querying data: " + query)
	rs = client.query(query)
	print ("ResultSet: %s" % rs)
	print ("Items %s" % rs.items())
	print ("Keys: %s" % rs.keys())
	
	
	return(rs.raw)