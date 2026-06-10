# ⚡ Smart Home Energy Monitoring System (IoT & Data Analytics Platform)

An industry-aligned, software-driven IoT project that simulates real-time electrical grid parameters and appliance load signatures. It utilizes edge-computing mathematical principles to compute power analytics, track dynamic energy consumption, estimate electricity billing, and manage automated grid overload safety alerts through a premium web dashboard.

## 📸 Production-Ready Live Dashboard Showcase

![Live Web Dashboard Layout](python_simulation/dashboard_screenshot.png)

## 🌟 Core Architecture & Technical Features
- **Deterministic Appliance Load Profiles:** Simulates realistic power draws based on real home appliances (AC, Refrigerator, Smart TV, Lights, Geyser) cycling ON/OFF dynamically with mathematical noise insertion.
- **Dynamic Voltage Fluctuations:** Replicates actual Indian power grid inconsistencies by fluctuating voltages realistically between $225\text{V}$ and $235\text{V}$.
- **Edge Analytics Pipeline:** Instantly computes Total Current Load ($I = \frac{P}{V}$), Active Power Demand (Watts), Cumulative Unit Consumption ($\text{kWh}$), and Running Financial Costs (INR).
- **Smart Overload Engine:** Evaluates live demand against a safe household threshold ($3.2\text{kW}$) and instantly trips the monitoring status to flag a critical overlay alert.
- **Structured Data Persistence:** Continuously logs structured telemetry data into a local CSV file, mimicking real time-series database (TSDB) storage transactions for historical audit reports.

## 🛠️ Complete Tech Stack
- **Core Simulation Engine:** Python 3.x
- **Visualization Web App Frontend:** Streamlit Framework
- **Data Structuring & Analytics:** Pandas Engine
- **Plotting Pipeline:** Matplotlib Time-Series Graphs

## 📂 Project Repository Directory Tree
```text
Smart-Home-Energy-Monitoring-System/
│
├── python_simulation/         # Executable Core Platform
│   ├── simulator.py           # Real-time appliance load generator script
│   └── dashboard.py           # Premium Streamlit web UI script
├── data/                      # Local Data Storage Layer
│   └── energy_log.csv         # Live updated historical telemetry log
├── firmware/                  # Reserved for Future ESP32 Deployment
│   └── hardware_notes.md      # Embedded systems architecture guide
├── docs/                      # Technical Documentation
│   └── architecture.md        # Hardware interface configuration mapping
├── requirements.txt           # Python software dependencies environment setup
└── README.md                  # Main developer documentation showcase

## 💻 Quick Start & Deployment Guide

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/smart-home-energy-monitoring-system.git](https://github.com/YOUR_USERNAME/smart-home-energy-monitoring-system.git)
cd smart-home-energy-monitoring-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Telemetry Stream (Terminal 1)
python python_simulation/simulator.py

# 4. Launch Web Dashboard (Terminal 2)
streamlit run python_simulation/dashboard.py
