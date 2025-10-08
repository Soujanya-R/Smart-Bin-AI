

# ♻️ EcoRoute AI Smart Bin Simulation Dashboard

Welcome to the EcoRoute AI Smart Bin Simulation Dashboard. This application serves as a comprehensive frontend interface to demonstrate the capabilities of the EcoRoute AI Smart Bin—a smart waste management system featuring autonomous internal segregation and route optimization data analytics.

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/Soujanya-R/Smart-Bin-AI/refs/heads/main/Screenshot%202025-10-08%20190601.png)

![App Screenshot](https://raw.githubusercontent.com/Soujanya-R/Smart-Bin-AI/refs/heads/main/Screenshot%202025-10-08%20190619.png)

![App Screenshot](https://raw.githubusercontent.com/Soujanya-R/Smart-Bin-AI/refs/heads/main/Screenshot%202025-10-08%20190731.png)

![App Screenshot](https://raw.githubusercontent.com/Soujanya-R/Smart-Bin-AI/refs/heads/main/Screenshot%202025-10-08%20190819.png)

![App Screenshot](https://raw.githubusercontent.com/Soujanya-R/Smart-Bin-AI/refs/heads/main/Screenshot%202025-10-08%20190835.png)


## ✨ Features


- This dashboard is built using React and provides a real-time visualization of the smart bin's operation and performance metrics.

- Intelligent Self-Sorting Demo: Visualize the core functionality where a single waste input is automatically analyzed and sorted into separate compartments (Paper, Plastic, Metal, Glass, Cardboard, Trash) using AI.

- Real-Time Simulation: An interactive component allowing users to "throw" items into the bin and observe the classification and segregation process.

- Analytics Dashboard: Displays key metrics, including:

  - Real-time Bin Capacity (via a visual chart).

  - Sorting Success Rates and Confidence Scores.

  - Total waste processed and historical activity log.

- Professional, Themed Interface: Supports responsive design and light/dark theme modes for optimal user experience.

- Product Overview Video: Dedicated section for embedding a product explainer video (currently set to a placeholder path).


## 📂 Project Structure

### This project follows a standard React structure, with core logic separated into reusable components.

```
EcoRouteAI_SmartBinSim/
└── frontend/
    ├── public/
    │   └── EcoRoute_Demo_40s.mp4 — Product demo video and other static assets.
    │
    ├── src/
    │   ├── components/
    │   │   ├── AnalyticsDashboard.js — Displays real-time charts, statistics, and bin capacity analytics.
    │   │   ├── Dashboard.js — Main wrapper that manages app state, theme toggling, and backend communication.
    │   │   ├── DemoContent.js — Shows the Smart Bin demo video and user-friendly product usage guide.
    │   │   └── ... — Additional components like Navbar, Footer, or VirtualBin.
    │
    │   ├── styles/
    │   │   ├── AnalyticsDashboard.css — Styling for dashboard charts and visual layouts.
    │   │   └── ProfessionalLayout.css — Global styles for layout, navbar, and professional theme consistency.
    │
    │   └── App.js — Root React component; initializes the app and renders Navbar + Dashboard.
    │
    └── package.json — Frontend dependencies, scripts, and project configuration.
```

## 🛠️ Prerequisites

1. This application requires two distinct components to function correctly: the frontend (this repository) and a separate AI Classification Backend.

2. Node.js and npm: Required to run the React application.

3. Python & Flask Backend: You must have your AI classification server (e.g., a simple Flask application that serves the image classification model) running simultaneously. The frontend expects this backend to be accessible, typically at http://127.0.0.1:5000, to handle the THROW ITEM requests.

## 🚀 Installation and Setup

1. Clone the Repository

        git clone <repository-url>
        cd EcoRouteAI_SmartBinSim/frontend


2. Install Dependencies
```bash 
npm install

```

3. Start the Flask Backend (Mandatory)

        Before starting the frontend, ensure your separate Flask classification server is running and listening on the port the React app expects (usually 5000).

        # Example command to start your Flask server (adjust as necessary)
python app.py


4. Run the Frontend Application

- Start the React development server:

        npm start


The application should open automatically in your browser at http://localhost:3000 (or another available port).
## 💡 Usage Instructions

- The DemoContent.js component guides the user through the simulation process, which relies on the backend being active.

- Ensure Backend is Live: Confirm your Python/Flask server is running.

- Choose Item: Use the designated input control to select a waste item image (e.g., a picture of paper, glass, or plastic).

- Activate Simulation: Click the 'THROW ITEM' button.

- Observe Classification: The frontend will send the image data to your Flask server. The system will display 'SCANNING...' and then animate the item being routed to one of the 6 segregated bins based on the classification result returned by the backend API.

- Review Data: Check the Activity Log and the Analytics Dashboard to see the new data point recorded and how the bin capacities change.
## 🎨 Styling and Theming

- The application utilizes a modular CSS approach for a professional look and feel.

- Theming: Theme logic (light/dark mode toggling and state) is primarily handled within the Dashboard.js component, which passes the currentTheme object as a prop down to child components.

- Layout: Global layout elements, including the fixed navigation bar, are styled using src/styles/ProfessionalLayout.css.

- Analytics Colors: Chart colors within AnalyticsDashboard.js are strictly defined and consistent across the six waste categories: Cardboard, Glass, Metal, Paper, Plastic, and Trash.

