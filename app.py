# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setup SQLite connection
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect DB into classes
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# Create variables for each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create SQLite Session
# session = Session(engine)

# Create Flask instance
app = Flask(__name__)

# Create first route (root/homepage)
    # Use "<br>" for newline/line break
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    <br>Available Routes:
    <br>/api/v1.0/precipitation
    <br>/api/v1.0/stations
    <br>/api/v1.0/tobs
    <br>/api/v1.0/temp/start/end
    ''')
# Create precipitaion route
    # the ".\" continues the qery to the next line
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}

    session.close()

    return jsonify(precip)

# Create stations route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))

    session.close()

    return jsonify(stations=stations)

# Create Temperature Observations (tob) route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))

    session.close()

    return jsonify(temps=temps)

# Create stats route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:

        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))

        session.close()

        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))

    session.close()

    return jsonify(temps=temps)