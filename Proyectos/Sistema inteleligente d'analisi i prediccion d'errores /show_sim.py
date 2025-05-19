import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from scripts.simulate_data import simulate, OUTPUT_PATH_SIMULATED
import json

class show_sim:
    def __init__(self):
        st.set_page_config(page_title="Hardware Simulator", layout="centered")
        self.simulator = simulate()
        self.placeholder = st.empty()

    def run(self):
        st.title("🛠️ Hardware Simualtor")

        with st.form("config_form"):
            st.subheader("⚙️ Siluamotor configuration")
            duration = st.slider("Total Time (seconds)", min_value=1, max_value=5000, value=1)
            interval = st.slider("Interval with samplers (seconds)", min_value=1, max_value=10, value=1)
            submitted = st.form_submit_button("Start Simulation")

        if submitted:
            self.run_simulation(duration, interval)

    def run_simulation(self, duration_seconds, interval):
        st.info(f"Start to simulation with {duration_seconds} seconds (every to {interval}s)...")

        samples = self.simulator.simulate_data(duration_seconds, interval)

        for sample in samples:
            self.display_sample(sample)

        st.success(f"✅ Finish simulation. File generated to: `{OUTPUT_PATH_SIMULATED}`")
        self.auto_close_browser()
        
        with open("status.json", "w") as f:
            json.dump({"done": True}, f)

    def display_sample(self, sample):
        with self.placeholder.container():
            st.subheader(f"📅 Timestamp: {sample['timestamp']}")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 💻 CPU")
                st.metric("CPU Usage (%)", sample["cpu_usage"])
                st.markdown("### 🧠 RAM")
                st.metric("RAM Usage (%)", sample["ram_usage"])
                st.markdown("### 🌡️ Temperatura")
                st.metric("Temp (°C)", sample["temperature"])

            with col2:
                st.markdown("### 💾 Disc")
                st.metric("Disk Usage (%)", sample["disk_usage"])
                st.markdown("### 🌐 Networl")
                st.metric("Network Latency (ms)", sample["network_latency"])
                st.markdown("### ⚠️ Error code")
                st.metric("Error Code", sample["error_code"])

            st.divider()

    def auto_close_browser(self):
      os.system('''osascript -e 
                'tell application "Google Chrome" 
                to close (windows whose name contains 
                "Hardware Simulator")' ''')

if __name__ == "__main__":
    simulator = show_sim()
    simulator.run()
   