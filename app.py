from flask import Flask, jsonify
from flask.wrappers import Response
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt


engine = create_engine("sqlite:///hawaii.sqlite")

base = automap_base()
base.prepare(engine, reflect=True)

Station = base.classes.station
Measurement = base.classes.measurement

app = Flask(__name__)


@app.route("/")
def welcome():
    """List of all available api routes"""

    return(
        f"Welcome to the weather API for Hawaii<br/>"
        f"--------------------------<br/>"
        f"Available Routes : <br/>"
        f"/api/v1.0/precipitation&emsp;&emsp;&nbsp;<span style=\"color: blue;\">[Description: Returns date and precipitation]</span><br/>"
        f"/api/v1.0/stations&emsp;&emsp;&emsp;&emsp;&nbsp;<span style=\"color: blue;\">[Description: Returns all station names]</span><br/>"
        f"/api/v1.0/tobs&emsp;&emsp;&emsp;&ensp;&emsp;&emsp;&nbsp;<span style=\"color: blue;\">[Description: Returns temperature of most active station in previous year]</span><br/>"
        f"/api/v1.0/startdate&emsp;&emsp;&emsp;&ensp;&ensp;<span style=\"color: blue;\">[Desciption: Returns TMIN,TMAX,TAVG after startdate]</span><br/>"
        f"/api/v1.0/startdate/enddate&ensp;<span style=\"color: blue;\">[Description: Returns TMIN,TMAX,TAVG between start and end date]</span><br/>"
        f"-----------------------------<br/>"
        f"date format : YYYY-MM-DD"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(bind=engine)

    result = session.query(Measurement).all()

    session.close()

    response = {}

    for row in result:
        response[row.date] = row.prcp

    return jsonify(response)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(bind=engine)

    result = session.query(Station).all()

    session.close()

    stations = [row.station for row in result]

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(bind=engine)

    result = session.query(Measurement.station, func.count(Measurement.station)).group_by(
        Measurement.station).order_by(func.count(Measurement.station).desc()).first()

    mostactive_station = result[0]

    result = session.query(Measurement).filter(Measurement.station == mostactive_station).\
        order_by(Measurement.date.desc()).limit(365).all()

    session.close()

    response = {}

    for row in result:
        response[row.date] = row.tobs

    return jsonify(response)


@ app.route("/api/v1.0/<start>")
def temperature_data(start):

    session = Session(bind=engine)

    recent = session.query(Measurement.date).order_by(
        Measurement.date.desc()).first()
    recent_date = dt.datetime.strptime(recent[0], '%Y-%m-%d').date()

    last = session.query(Measurement.date).order_by(
        Measurement.date.asc()).first()
    last_date = dt.datetime.strptime(last[0], '%Y-%m-%d').date()

    query_date = dt.datetime.strptime(start, '%Y-%m-%d').date()

    if (query_date >= last_date) and (query_date <= recent_date):

        sel = [func.min(Measurement.tobs), func.avg(
            Measurement.tobs), func.max(Measurement.tobs)]

        result = session.query(
            *sel).filter(Measurement.date >= query_date).all()

        session.close()

        response = {"TMIN": result[0][0],
                    "TAVG": result[0][1],
                    "TMAX": result[0][2]}

        return jsonify(response)
    else:
        return f"error:date not found"


@ app.route("/api/v1.0/<start>/<end>")
def temperature_data_stat(start, end):
    session = Session(bind=engine)

    recent = session.query(Measurement.date).order_by(
        Measurement.date.desc()).first()
    recent_date = dt.datetime.strptime(recent[0], '%Y-%m-%d').date()

    last = session.query(Measurement.date).order_by(
        Measurement.date.asc()).first()
    last_date = dt.datetime.strptime(last[0], '%Y-%m-%d').date()

    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()

    if (start_date >= last_date) and (start_date <= recent_date) and (end_date >= last_date) and (end_date <= recent_date):

        sel = [func.min(Measurement.tobs), func.avg(
            Measurement.tobs), func.max(Measurement.tobs)]

        result = session.query(*sel).filter(Measurement.date >=
                                            start).filter(Measurement.date <= end).all()

        session.close()

        response = {"TMIN": result[0][0],
                    "TAVG": result[0][1],
                    "TMAX": result[0][2]}

        return jsonify(response)
    else:
        return f"error: date not found"


if __name__ == "__main__":
    app.run(debug=True)
