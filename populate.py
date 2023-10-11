import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from faker import Faker
import random

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

provider_department = ['Cardiology', 'Immunology' 'Neurology', 'Pediatrics', 
                   'Orthopedics', 'Gastroenterology' 'Radiology', 'Nephrology' 'Internal Medicine']
provider_occupation_title = ['Physician', 'Nurse Practitioner', 'Physician Assistant', 'Occupational Therapist','Physical Therapist']

def insert_fake_data(engine, num_providers=50, num_patients=100):
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into providers
        for _ in range(num_providers):
            first_name = fake.first_name()
            last_name = fake.last_name()
            provider_department = random.choice(provider_department)
            provider_occupation_title = random.choice (provider_occupation_title)
            connection.execute(f"INSERT INTO providers (first_name, last_name, provider_department, provider_occupation_title) VALUES ('{first_name}', '{last_name}', '{provider_department}', '{provider_occupation_title}')") # Noqa: E501
        

        # Fetch all provider IDs
        provider_ids = [row[0] for row in connection.execute("SELECT provider_id FROM providers").fetchall()] # Noqa: E501
        # Fetch all patient IDs
        patient_ids = [row[0] for row in connection.execute("SELECT patient_id FROM patients").fetchall()] # Noqa: E501
        
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=7, maximum_age=95)
            provider_id = random.choice(provider_ids)
            connection.execute(f"""INSERT INTO patients (first_name, last_name, date_of_birth, provider_id) VALUES ('{first_name}', '{last_name}', '{date_of_birth}', {provider_id})""") # Noqa: E501
   
if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")