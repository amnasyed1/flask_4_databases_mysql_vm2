from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Create a connection string

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'

# Create engine

engine = create_engine(
        connection_string,
        connect_args=connect_args,
)
#creating a flask app

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/providers')
def providers():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM providers')
        result1 = connection.execute(query1)
        db_data1 = result1.fetchall()
    return render_template('providers.html', data1=db_data1)

@app.route('/patients')
def patients():
    with engine.connect() as connection:
        query2 = text('SELECT * FROM patients')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('patients.html', data2=db_data2)
    

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )