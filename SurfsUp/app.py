# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/measurements<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

#####Get the precipitation data for the last year, store via dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    #session = Session(engine)

    results = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date >= prev_year).all()
    session.close()

    #Do i even need a loop?
    precip = {date:prcp for prcp, date in results}
    return jsonify(precip)



#####list all stations as a Json object
@app.route("/api/v1.0/stations")
def Station_data():
    #How could I list them in descending order?
    # Query all passengers
    results = session.query(Station.station, Station.name).all()

    session.close()
    stations = list(np.ravel(results))
    return jsonify(stations)

#session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()
    #if we need to change a tuple to a list
    #all_stations = list(np.ravel(results)
    #return jsonify(all_stations)



#####return a JSON list for the temps in the last year from the most active station
@app.route("/api/v1.0/tobs")
def tobs():
    temps = session.query(Measurement.tobs).filter(Measurement.date >= dt.date(2016, 8, 23)).\
                        filter(Measurement.station == 'USC00519281').all()
    session.close()
    temperatures = {"Temperatures in the last year" : list(np.ravel(temps))}
    return jsonify(temperatures)

## this route accepts user input
## the user provides start date and end date
#####Calculate min, mean, and max for those temps

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def startend(start=None, end=None):
    partail_query = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        start = dt.datetime.strptime(start,"%Y%m%d")
        results = session.query(*partail_query).filter(Measurement.date >= start).all()
        session.close()
        temps = list(np.ravel(results))
        return jsonify(temps)
    start = dt.datetime.strptime(start,"%Y%m%d")
    end = dt.datetime.strptime(end,"%Y%m%d")

    results = session.query(*partail_query).filter(Measurement.date >= start).filter(Measurement.date<=end).all()
    session.close()
    temps = list(np.ravel(results))
    return jsonify(temps)


if __name__ == "__main__":
    app.run(debug=True)
