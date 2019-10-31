from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Weater API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
    )


@app.route("/api/v1.0/precipitation/")
def get_precipitation():
    conn = engine.connect()
    
    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                """

    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/precipitation/<start_date>/<end_date>")
def get_precipitation_forDates(start_date, end_date):
    conn = engine.connect()

    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                WHERE
                    date > '{start_date}'
                    AND date <= '{end_date}'
                """
    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())
    
if __name__ == "__main__":
    app.run(debug=True)