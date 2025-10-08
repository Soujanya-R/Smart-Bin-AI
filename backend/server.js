const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const sqlite3 = require("sqlite3").verbose();
const path = require("path");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());
const tf = require('@tensorflow/tfjs-node');

async function loadModel() {
  const model = await tf.loadLayersModel('file://backend/waste_cnn_model/model.json');
  return model;
}

async function classifyImage(imagePath) {
  const model = await loadModel();
  const imageBuffer = fs.readFileSync(imagePath);
  const tensor = tf.node.decodeImage(imageBuffer)
    .resizeNearestNeighbor([128,128])
    .expandDims()
    .toFloat()
    .div(tf.scalar(255.0));

  const prediction = model.predict(tensor);
  const scores = prediction.dataSync();
  const categories = ["Plastic", "Paper", "Metal", "Glass", "Organic"]; // adjust to your dataset
  const maxIndex = scores.indexOf(Math.max(...scores));

  return { category: categories[maxIndex], confidence: scores[maxIndex].toFixed(2) };
}


// SQLite DB
const db = new sqlite3.Database("./wasteLog.db", (err) => {
  if (err) console.error(err.message);
  else console.log("Connected to SQLite database.");
});

// Create table if not exists
db.run(
  `CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    confidence REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
  )`
);

// Mock AI endpoint
app.post("/classify-item", (req, res) => {
  const { itemName } = req.body;

  const categories = ["Plastic", "Paper", "Organic", "Metal", "E-waste"];
  const category = categories[Math.floor(Math.random() * categories.length)];
  const confidence = (Math.random() * 0.3 + 0.7).toFixed(2); // 0.7-1.0

  // Insert into DB
  db.run(
    `INSERT INTO items(name, category, confidence) VALUES (?, ?, ?)`,
    [itemName, category, confidence],
    function (err) {
      if (err) return res.status(500).json({ error: err.message });
      res.json({ id: this.lastID, category, confidence });
    }
  );
});

// Fetch all items for dashboard/log
app.get("/waste-items", (req, res) => {
  db.all(`SELECT * FROM items ORDER BY timestamp DESC`, [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

// Dashboard data (category counts)
app.get("/dashboard-data", (req, res) => {
  db.all(
    `SELECT category, COUNT(*) as count FROM items GROUP BY category`,
    [],
    (err, rows) => {
      if (err) return res.status(500).json({ error: err.message });
      res.json(rows);
    }
  );
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
