from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Blueprint
from PIL import Image
import numpy as np
from keras.models import load_model
import tensorflow as tf
from tensorflow import keras

# app = Flask(__name__)
app = Blueprint('predict', __name__)
CORS(app)  # Enable CORS for all origins

# predict_app = Blueprint('predict_app', __name__)

# Load your deep learning model
model = load_model('skin_disease_vgg16.h5')

# Define image width and height
img_width, img_height = 256, 256

# Define a function to preprocess the image
def preprocess_image(image):
    # Resize image to match model input size
    image = image.resize((img_width, img_height))
    # Convert image to numpy array
    image_array = np.array(image) / 255.0  # Normalize pixel values
    return image_array

# Define a function to make predictions
def predict_image(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Make prediction using the model
    predictions = model.predict(np.expand_dims(processed_image, axis=0))
    return predictions

# Define a route to handle image uploads
@app.route('/predict', methods=['POST','OPTIONS'])
def predict():
    # Check if request contains file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    # Check if the file is an image
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        image = Image.open(file)
        # Make prediction
        predictions = predict_image(image)

        # return jsonify({'predicted_class_index': int(max_index)})
        return jsonify({'predictions': predictions.tolist()})
    else:
        return jsonify({'error': 'Invalid file type'})

# if __name__ == '__main__':
#      app.run(port=3005, debug=True)

# def get_blueprint():
#     return predict_app