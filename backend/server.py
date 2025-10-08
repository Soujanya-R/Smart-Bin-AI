from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import sqlite3

# --- App setup ---
app = Flask(__name__)
CORS(app)

# --- Model ---
MODEL_PATH = "waste_cnn_model.h5"
IMG_SIZE = (128, 128)
CLASS_NAMES = sorted(os.listdir("dataset"))  # folders: cardboard, glass, plastic, etc.
model = load_model(MODEL_PATH)

# --- Database ---
DB_PATH = "D:/EcoRouteAI_SmartBinSim/backend/wasteLog.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS items
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              category TEXT,
              confidence REAL,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

# --- Routes ---
@app.route("/classify-item", methods=["POST"])
def classify_item():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save temporary
    temp_path = os.path.join("temp_upload.jpg")
    file.save(temp_path)

    # Preprocess image
    img = image.load_img(temp_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    predictions = model.predict(img_array)[0]
    max_index = np.argmax(predictions)
    category = CLASS_NAMES[max_index]
    confidence = float(predictions[max_index])

    # Remove temp file
    os.remove(temp_path)

    # SAVE TO DATABASE
    c.execute(
        "INSERT INTO items (name, category, confidence) VALUES (?, ?, ?)",
        (file.filename, category, confidence)
    )
    conn.commit()
    item_id = c.lastrowid

    return jsonify({
        "id": item_id,
        "category": category,
        "confidence": round(confidence, 2),
        "filename": file.filename
    })

@app.route("/waste-items", methods=["GET"])
def get_waste_items():
    c.execute("SELECT id, name, category, confidence FROM items ORDER BY timestamp DESC")
    rows = c.fetchall()
    items = []
    for row in rows:
        items.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "confidence": row[3]
        })
    return jsonify(items)


@app.route("/dashboard-data", methods=["GET"])
def dashboard_data():
    c.execute("SELECT category, COUNT(*) FROM items GROUP BY category")
    data = [{"category": row[0], "count": row[1]} for row in c.fetchall()]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
