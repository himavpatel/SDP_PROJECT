from flask import Flask, Blueprint
from flask_cors import CORS
from predict import app as predict_blueprint
from login import app as login_blueprint
# from appointment import app as appointment_blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Register blueprints
app.register_blueprint(predict_blueprint)
app.register_blueprint(login_blueprint)
# app.register_blueprint(appointment_blueprint)

if __name__ == '__main__':
    app.run( port=3005,debug=True)