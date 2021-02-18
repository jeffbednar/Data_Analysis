import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

session=Session(engine)

app = Flask(__name__)

@app.route('/')
def home():
    return (
       
        f"<h1>Available Routes:</h1><br/><br/>"
        f"<h2>/api/v1.0/precipitation</h2><br/>"
        f"<h2>/api/v1.0/stations</h2><br/>"
        f"<h2>/api/v1.0/tobs</h2><br/>"
        f"<h2>/api/v1.0/<start></h2><br/>"
        f"<h2>/api/v1.0/<start>/<end></h2>"
    )
    
@app.route('/api/v1.0/precipitation')
def percipitation():
    
    one_year_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    
    precipitation_data = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= one_year_date).\
        order_by(measurement.date).all()

    precipitation_dict = dict(precipitation_data)
        
    return jsonify(precipitation_dict)

@app.route('/api/v1.0/stations')
def stations():
    all_stations = session.query(station.station, station.name).all()

    station_list = list(all_stations)

    return jsonify(station_list)

@app.route('/api/v1.0/tobs')
def tobs():
    one_year_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    
    most_active_station_tobs = session.query(measurement.date, measurement.tobs).\
    filter(measurement.date >= one_year_date).\
    filter(measurement.station == 'USC00519281').\
    order_by(measurement.date).all()

    most_active_station_tobs_list = list(most_active_station_tobs)

    return jsonify(most_active_station_tobs_list)

@app.route('/api/v1.0/<start>')
def start(start):
    start_date = session.query(measurement.date, func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= start).\
        group_by(measurement.date).all()
    start_date_list = list(start_date)

    return jsonify(start_date_list)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start, end):
    start_end_date = session.query(measurement.date, func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).\
        group_by(measurement.date).all()
    start_end_list = list(start_end_date)

    return jsonify(start_end_list)

if __name__ == "__main__":
    app.run(debug=True)