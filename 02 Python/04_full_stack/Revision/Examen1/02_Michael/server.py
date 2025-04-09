from flask_app import app
from flask_app.controllers import usuarios_controller, asesorias_controller  # Importar asesorias_controller en lugar de eventos_controller

if __name__ == "__main__":
    app.run(debug=True)