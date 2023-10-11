from flask import Flask, render_template
import pandas as pd
import random 
from faker import Faker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)
fake = Faker()

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/providers')
def providers():
    providers_sql_query = "SELECT * FROM providers"
    df_providers = read_sql(providers_sql_query, db_engine)
    provider_data = df_providers.to_dict(orient='records')  
    return render_template('providers.html', data =provider_data)    

@app.route('/patients')
def patients():
    patients_sql_query = "SELECT * FROM patients"
    df_patients = read_sql(patients_sql_query, db_engine)
    patient_data = df_patients.to_dict(orient='records')
    return render_template('patients.html', data =patient_data)
    

if __name__ == '__main__':
    app.run(debug=True)