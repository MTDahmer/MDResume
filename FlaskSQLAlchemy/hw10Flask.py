from flask import Flask, jsonify
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

surfer = Flask(__name__)
@surfer.route("/")
def available():
    return (
        f"Available Routes:"
        f"/api/precipitation"
        f"/api/stations"
        f"/api/temperature"
        f"/api/<start>"
    )
@surfer.route("/api/precipitation")
def precipitation():
    query_dateS = dt.date(2017, 8, 23)
    query_dateF = dt.date(2016, 8, 23)
    # Perform a query to retrieve the data and precipitation scores
    twelveMonth = session.query(Measurement.prcp, Measurement.date).\
    filter(Measurement.date < query_dateS).\
    filter(Measurement.date > query_dateF).all()  
    return jsonify(twelveMonth)
@surfer.route("/api/stations")
def stations():
    stations = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    return jsonify(stations)
@surfer.route("/api/temperature")
def temp():
    query_dateS = dt.date(2017, 8, 23)
    query_dateF = dt.date(2016, 8, 23)
    twelveMonthtemp = session.query(Measurement.tobs, Measurement.date).\
    filter(Measurement.date < query_dateS).\
    filter(Measurement.date > query_dateF).\
    filter(Measurement.station == 'USC00519281').all()
    return jsonify(twelveMonthtemp)
#@surfer.route("/api/<start>")

#@surfer.route("/api/<start>/<end>")

if __name__ == '__main__':
    surfer.run(debug = True) 