# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/measurements<br/>"
        f"/api/v1.0/station<br/>"
    )


@app.route("/")
def index():
        return 'Search Hawaii'

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    session = Session(engine)

    results = session.query(Measurement.prcp, measurement.date).all()
    session.close()

    #
    year_precipitation = []
    for prcp in results:
        #set the date parameters below
        if measurement.date > "2016-08-23":
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = precipitation
        year_precipitation.append(prcp_dict)

    return jsonify(prcp_dict)

#list all stations as a Json object
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Query all passengers
    results = session.query(stations.station, stations.name).all()

    session.close()

session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()
#if we need to change a tuple to a list
    #all_stations = list(np.ravel(results)
    #return jsonify(all_stations)


#return a JSON list for the temps in the last year from the most active station
@app.route("/api/v1.0/tobs")
def tobs():
     

#Calculate min, mean, and max for those temps
@app.route("/api/v1.0/<start>/<end>")


#how to Jsonify something
@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)

if __name__ == "__main__":
    app.run(debug=True)
