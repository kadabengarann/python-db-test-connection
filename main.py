import os
from pprint import pprint
from flask import Flask, render_template
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

# Load environment variables from the .env file
load_dotenv()
USING_DB = os.getenv('USING_DB', 'True').lower() == 'true'
if USING_DB:
    # Get the database URI from the environment variables
    URI = os.getenv('DB_URI')
    DB_URI = URI
    
    engine = create_engine(DB_URI)
    
    connection = engine.connect()
    
    print("DB connection successful!!")
    
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    # Print the list of tables
    print("Tables in the database:")
    print(tables)
else:
    tables = []

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flask Application!"

@app.route("/tables")
def list_tables():
    if USING_DB:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        return render_template('tables.html', tables=tables)
    else:
        return "Database connection is disabled."

if __name__ == "__main__":
    app.run(port="4269")
