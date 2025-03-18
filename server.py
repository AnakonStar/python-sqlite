from flask import Flask
from modules.laudo.controllers.laudo_controller import initController
from datetime import datetime
from dotenv import load_dotenv
import os
from db.schema import generate_tables

app = Flask(__name__)

load_dotenv()

# Load environment variables from .env file

pythonport = os.getenv("PYTHON_PORT", "5000")
debugstate = os.getenv("DEBUG_STATE", "False").lower() == "true"

generate_tables()

initController(app)

@app.route("/teste")
def teste():
    current_date = datetime.now()
    return "<html><body><p>OK " + str(current_date) + "</p></body></html>"
                
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(pythonport), debug=debugstate)
