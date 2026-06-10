import time
import csv
import random
from datetime import datetime

# Real-world Appliance Specs (Load Signatures in Watts & Typical States)
APPLIANCES = {
    "Base Load (WiFi + Router)": {"power": 30, "prob_on": 1.0},
    "LED Lights & Fans": {"power": 180, "prob_on": 0.8},
    "Refrigerator": {"power": 250, "prob_on": 0.6},  # Cycles ON/OFF
    "Smart TV & Soundbar": {"power": 150, "prob_on": 0.4},
    "Laptop Charger": {"power": 65, "prob_on": 0.5},
    "Air Conditioner (1.5 Ton)": {"power": 1800, "prob_on": 0.3},
    "Water Geyser": {"power": 2000, "prob_on": 0.1}
}

ELECTRICITY_RATE_PER_KWH = 7.5  # ₹ per kWh
OVERLOAD_THRESHOLD_WATTS = 3200.0  # Safe grid limit for home

# Initialize CSV File with enhanced professional structure
with open('../data/energy_log.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Timestamp', 'Grid Voltage (V)', 'Total Current (A)', 
        'Active Power (W)', 'Cumulative Energy (kWh)', 
        'Running Cost (INR)', 'Active Appliances', 'Alert Status'
    ])

cumulative_wh = 0.0
time_step_hours = 2 / 3600.0  # 2-second telemetry window

print("=========================================================================================")
print("               INDUSTRIAL SMART HOME ENERGY MANAGEMENT SYSTEM (EDGE NODE)                ")
print("=========================================================================================")
print(f"{'Timestamp':<20} | {'Voltage':<7} | {'Current':<7} | {'Power (W)':<9} | {'Energy (kWh)':<12} | {'Cost':<7} | {'Status':<15}")
print("-----------------------------------------------------------------------------------------")

try:
    while True:
        # 1. Simulate Realistic Voltage Fluctuations (225V - 235V)
        voltage = round(random.uniform(225.0, 235.0), 1)
        
        # 2. Simulate Appliance State Machine (Dynamic load profiles)
        active_power = 0
        active_list = []
        
        for name, spec in APPLIANCES.items():
            # Base load is always ON, others cycle based on probability
            if spec["prob_on"] == 1.0 or random.random() < spec["prob_on"]:
                active_power += spec["power"]
                active_list.append(name.split(" ")[0]) # Get short name
        
        # Add slight minor electrical noise to power
        active_power += round(random.uniform(-15, 15), 1)
        if active_power < 0: active_power = 30
            
        # 3. Calculate Derived Metrics (Ohm's & Power Law)
        # Current I = P / V
        current = round(active_power / voltage, 2)
        
        # Energy accumulation
        energy_consumed_kwh = (active_power * time_step_hours) / 1000.0
        cumulative_wh += (active_power * time_step_hours)
        cumulative_kwh = cumulative_wh / 1000.0
        
        # Financial cost model
        running_cost = round(cumulative_kwh * ELECTRICITY_RATE_PER_KWH, 2)
        
        # 4. Smart Alert Engine
        alert_status = "NORMAL"
        if active_power > OVERLOAD_THRESHOLD_WATTS:
            alert_status = "⚠️ OVERLOAD ALERT"
            
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        appliances_str = ", ".join(active_list)
        
        # 5. Print Styled Dashboard to Console
        print(f"{timestamp} | {voltage:<5}V | {current:<5}A | {active_power:<9.1f} | {cumulative_kwh:<12.5f} | ₹{running_cost:<5} | {alert_status:<15}")
        
        # 6. Log Structured Analytics to CSV
        with open('../data/energy_log.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp, voltage, current, round(active_power, 1), 
                round(cumulative_kwh, 5), running_cost, appliances_str, alert_status
            ])
            
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[INFO] Edge Node safely disconnected. Metrics archived in 'data/energy_log.csv'.")