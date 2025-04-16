import random
import time
import json
from datetime import datetime
import os
from scripts.var_constant import OUTPUT_PATH_SIMULATED

class simulate:
    def generate_sample(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "cpu_usage": round(random.uniform(10, 95), 2),
            "ram_usage": round(random.uniform(20, 90), 2),
            "disk_usage": round(random.uniform(30, 99), 2),
            "temperature": round(random.uniform(30, 85), 2),
            "network_latency": round(random.uniform(1, 200), 2),
            "error_code": random.choice(["OK", "WARN", "ERR", "CRIT"])
        }
    def simulate_data(self,duration_seconds=60, interval=5):
        os.makedirs(os.path.dirname(OUTPUT_PATH_SIMULATED), exist_ok=True)
        with open(OUTPUT_PATH_SIMULATED, "w") as f:
            for _ in range(0, duration_seconds, interval):
                sample = self.generate_sample()
                f.write(json.dumps(sample) + "\n")
                print("Generated:", sample)
                time.sleep(interval)



