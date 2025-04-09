import os
from flask_app import app
from flask_app.controllers import asesorias
from flask_app.controllers import autentificacion 



if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"), port=os.getenv("PUERTO"))
