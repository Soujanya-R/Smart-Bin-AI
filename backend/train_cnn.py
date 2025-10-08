# backend/train_cnn.py
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt

# Dataset path (no train/test split manually)
data_dir = "dataset"   # go up one level from backend to dataset

# Parameters
img_size = (128, 128)
batch_size = 32
epochs = 10  # increase if you have GPU/time

# Data preprocessing with validation split
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,       # rotate images up to 30 degrees
    width_shift_range=0.2,   # shift horizontally
    height_shift_range=0.2,  # shift vertically
    shear_range=0.2,         # shear transformations
    zoom_range=0.2,          # random zoom
    horizontal_flip=True,    # mirror images
    fill_mode='nearest',
    validation_split=0.2
)


train_data = datagen.flow_from_directory(
    data_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode="categorical",
    subset="training"
)

val_data = datagen.flow_from_directory(
    data_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode="categorical",
    subset="validation"
)

# CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(128,128,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation="relu"),
    MaxPooling2D(2,2),
    Conv2D(256, (3,3), activation="relu"),  # new deeper layer
    MaxPooling2D(2,2),
    Flatten(),
    Dense(256, activation="relu"),
    Dropout(0.5),
    Dense(train_data.num_classes, activation="softmax")
])


model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Train
history = model.fit(train_data, validation_data=val_data, epochs=epochs)

# Save trained model in backend folder
model.save("waste_cnn_model.h5")

# Plot accuracy
plt.plot(history.history["accuracy"], label="train_acc")
plt.plot(history.history["val_accuracy"], label="val_acc")
plt.legend()
plt.show()
