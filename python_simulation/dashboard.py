import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="IoT Energy Dashboard", layout="wide")

# Custom Premium CSS Styling
st.markdown("""
    <style>
    .main-title {
        text-align: center; 
        color: #FF4B4B; 
        font-family: 'Arial Black', Gadget, sans-serif;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>⚡ SMART HOME ENERGY MONITORING SYSTEM</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #888; margin-bottom: 25px;'>Edge Computing Telemetry Stream & Real-Time Analytics Dashboard</h5>", unsafe_allow_html=True)
st.write("---")

# Sidebar - Static Container Setup
st.sidebar.markdown("## 🛡️ System Control Center")
status_sidebar = st.sidebar.empty() 

kpi_zone = st.empty()

st.write("---")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 📈 Live Power Demand Curve (Watts)")
    chart_placeholder = st.empty()

with col_right:
    st.markdown("### 🔌 Active Load Profiles")
    appliance_placeholder = st.empty()

st.write("---")
st.markdown("### 📋 System Telemetry Log History")
table_placeholder = st.empty()

# Telemetry Real-time Loop
while True:
    try:
        df = pd.read_csv('../data/energy_log.csv')
        if not df.empty:
            last_row = df.iloc[-1]
            
            # 1. Update Sidebar Status
            if "⚠️" in str(last_row['Alert Status']) or "OVERLOAD" in str(last_row['Alert Status']):
                status_sidebar.error("🚨 CRITICAL ALERT:\nSYSTEM OVERLOAD DETECTED!")
            else:
                status_sidebar.success("✅ GRID STATUS: STABLE\nLoad is within safety limits.")
            
            with kpi_zone.container():
                k1, k2, k3, k4 = st.columns(4)
                k1.metric(label="Grid Voltage", value=f"{last_row['Grid Voltage (V)']} V", delta="±1.5V Fluctuation")
                k2.metric(label="Total Current Load", value=f"{last_row['Total Current (A)']} A")
                k3.metric(label="Active Power Consumption", value=f"{last_row['Active Power (W)']} W")
                k4.metric(label="Accrued Bill Amount", value=f"₹ {last_row['Running Cost (INR)']}", delta=f"{round(last_row['Cumulative Energy (kWh)'], 4)} kWh")
            
            # 2. Dynamic Technical Chart Generation
            fig, ax = plt.subplots(figsize=(8, 3.5))
            plot_df = df.tail(15) 
            
            ax.plot(plot_df['Timestamp'].str.split(' ').str[-1], plot_df['Active Power (W)'], marker='o', color='#FF4B4B', linewidth=2.5, label="Active Load")
            ax.axhline(y=3200.0, color='red', linestyle='--', alpha=0.7, label="Overload Limit (3.2kW)")
            
            ax.set_ylabel("Power (Watts)", fontsize=10)
            ax.set_xlabel("Timestamp Telemetry", fontsize=10)
            plt.xticks(rotation=45, fontsize=8)
            plt.yticks(fontsize=8)
            ax.grid(True, linestyle=':', alpha=0.5)
            ax.legend(loc="upper left", fontsize=8)
            
            chart_placeholder.pyplot(fig)
            plt.close(fig)
            
            # 3. Show Current Connected Appliances
            apps = str(last_row['Active Appliances']).split(", ")
            app_markdown = ""
            for app in apps:
                app_markdown += f"- 🔸 **{app}** is currently consuming power.\n"
            appliance_placeholder.markdown(app_markdown)
            
            # 4. Continuous Data Log Table
            table_placeholder.dataframe(df.tail(8)[['Timestamp', 'Grid Voltage (V)', 'Active Power (W)', 'Alert Status']], use_container_width=True)
                
    except Exception as e:
        pass
    
    time.sleep(2)