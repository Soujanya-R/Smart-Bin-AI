import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model("waste_cnn_model.h5")

# Class labels (same as your dataset folders)
class_labels = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

# Load one test image (change path to any image from your dataset)
img_path = r"D:\EcoRouteAI_SmartBinSim\backend\dataset\cardboard\cardboard1.jpg"
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0  # normalize

# Predict
predictions = model.predict(img_array)
predicted_class = class_labels[np.argmax(predictions)]
confidence = np.max(predictions) * 100

print(f"Predicted: {predicted_class} ({confidence:.2f}% confidence)")
