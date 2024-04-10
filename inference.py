import tensorflow as tf
import numpy as np
import json
import requests

SIZE = 32  # Update the size to match the input size of the model
MODEL_URI = 'http://localhost:8501/v1/models/pets:predict'
CLASSES = [str(i) for i in range(43)]

def preprocess_image(image_path):
    # Load the image in grayscale and resize it to match the model's input size
    image = tf.keras.preprocessing.image.load_img(
        image_path, color_mode='grayscale', target_size=(SIZE, SIZE)
    )
    # Convert the image to an array
    image = tf.keras.preprocessing.image.img_to_array(image)
    # Normalize the grayscale image
    image = (image - 128) / 128
    # Expand the dimensions to create a batch of size 1
    image = np.expand_dims(image, axis=0)
    return image

def get_prediction(image_path):
    # Preprocess the image
    image = preprocess_image(image_path)
    
    # Prepare the request data
    data = json.dumps({'instances': image.tolist()})
    
    # Make the prediction request
    response = requests.post(MODEL_URI, data=data.encode())
    result = json.loads(response.text)
    
    # Print the contents of the result dictionary
    print("Result:", result)
    
    # Get the predicted class index
    prediction = np.squeeze(result['predictions'][0])
    class_index = np.argmax(prediction)
    
    # Get the class name corresponding to the predicted index
    class_name = CLASSES[class_index]
    return class_name



