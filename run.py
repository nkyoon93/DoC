#1st script for program start
#pwd: /project_name/run.py
#flask is for easy api web ( like remote controller)
from app import app

app.run(host="0.0.0.0", port=8001)