import os
from pprint import pprint
from flask import Flask
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

# Load environment variables from the .env file
load_dotenv()

# Get the database URI from the environment variables
URI = os.getenv('DB_URI')
DB_URI = URI

# Create the SQLDatabase object from the URI
db = SQLDatabase.from_uri(DB_URI)

# Create an engine using SQLAlchemy
engine = create_engine(DB_URI)

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flask Application!"

@app.route("/tables")
def list_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return "<br>".join(tables)

if __name__ == "__main__":
    app.run(port="4269")
