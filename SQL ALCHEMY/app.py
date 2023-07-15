# import psycopg2
import csv_to_sqlite
import numpy as np
import pandas as pd
import csv
import json
 
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,text
from sqlalchemy.ext.asyncio import create_async_engine
from flask import Flask,request, jsonify


# Create a connection to the PostgreSQL database


engine = create_engine('postgresql://postgres:Rajan81@localhost:5432/EV_DB')

# engine = create_engine('postgresql://postgres:yWarBFw-sA@Kx@7@localhost:5432/EV_DB')
connection = engine.connect()


app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/data<br/>"
    )   
   

@app.route('/api/data', methods=['GET'])
def get_data():
   
    with open("EVcharge.csv") as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        #convert each row into a dictionary
        #and add the converted data to the data_variable
        data_dict = {}

        for rows in csv_reader:
            # print(rows)

            #assuming a column named 'No'1
            #to be the primary key
            StationName = rows["StationName"]
            data_dict[StationName] = rows
 
 
    return jsonify(data_dict )


if __name__ == "__main__":
     app.run(debug=True)
