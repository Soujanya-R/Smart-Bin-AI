const sqlite3 = require("sqlite3").verbose();
const path = require("path");

// Database file path
const dbPath = path.resolve(__dirname, "wasteLog.db");

// Connect to SQLite database
const db = new sqlite3.Database(dbPath, (err) => {
  if (err) console.error("DB Connection Error:", err);
  else console.log("Connected to SQLite database");
});

// Create table if not exists
db.run(
  `CREATE TABLE IF NOT EXISTS waste_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    confidence REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
  )`
);

module.exports = db;
