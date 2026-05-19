import os
from pathlib import Path

# Base directory for the LabOps-Sync project
base_dir = Path("LabOps_Sync")

# Step 1: Create Enterprise-Ready Layout
structure = [
    "config", 
    "reports", 
    "src", 
    "logs", 
    "data/exports"
]

print("Assembling LabOps-Sync Enterprise Logic...")
for folder in structure:
    (base_dir / folder).mkdir(parents=True, exist_ok=True)

files = {}

# 1. requirements.txt
files["requirements.txt"] = """
pydantic>=2.0.0
pandas>=2.0.0
""".strip()

# 2. src/reporter.py (Logic: Automated Markdown Generation)
files["src/reporter.py"] = """
import pandas as pd
from datetime import datetime
from pathlib import Path

class LabReportGenerator:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        
    def generate_batch_report(self, batch_id, stats, anomalies):
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        status = "⚠️ INVESTIGATION REQUIRED" if anomalies > 0 else "✅ COMPLIANT"
        
        content = f\"\"\"
# 🧪 LabOps-Sync: Batch Analysis Report
**Batch ID:** {batch_id}
**Timestamp:** {report_time}
---
### 📊 Process Analytics Summary
- **Mean Temperature:** {stats['temp']:.2f}°C
- **Mean PH Level:** {stats['ph']:.2f}
- **Projected Yield Accuracy:** {stats['yield']:.2f}%

### 🚨 Compliance & Safety Audit
- **Critical Anomalies Detected:** {anomalies}
- **Operational Status:** {status}
---
*Automated Report by PharmaTrack AI System*
\"\"\"
        report_path = self.output_dir / f"Report_{batch_id}.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        return report_path
""".strip()

# 3. src/sync_engine.py (Logic: Cloud-Ready Data Export)
files["src/sync_engine.py"] = """
import json
from pathlib import Path

class DataSyncEngine:
    def __init__(self, export_dir):
        self.export_dir = Path(export_dir)
        
    def export_for_cloud(self, df, batch_id):
        # Converting dataframe to Cloud-standard JSON format
        payload = df.to_dict(orient='records')
        export_path = self.export_dir / f"sync_payload_{batch_id}.json"
        with open(export_path, "w") as f:
            json.dump(payload, f, indent=4)
        return export_path
""".strip()

# 4. main_sync.py (The Orchestrator)
files["main_sync.py"] = """
import pandas as pd
from src.reporter import LabReportGenerator
from src.sync_engine import DataSyncEngine

def main():
    print("Initiating LabOps-Sync Final Orchestrator...")
    
    # Simulating data flow from P1 and P2
    mock_data = pd.DataFrame({
        'PH': [7.2, 7.15, 7.22],
        'Temperature': [37.1, 37.4, 37.0]
    })
    
    # 1. Generate Executive Report
    stats = {
        'ph': mock_data['PH'].mean(),
        'temp': mock_data['Temperature'].mean(),
        'yield': 84.96  # Static result from Project 2 success!
    }
    
    reporter = LabReportGenerator("reports")
    report_path = reporter.generate_batch_report("B-2026-X74", stats, anomalies=2)
    print(f"SUCCESS: Lab Report generated at {report_path}")
    
    # 2. Sync Data to Export Layer
    sync = DataSyncEngine("data/exports")
    sync_path = sync.export_for_cloud(mock_data, "B-2026-X74")
    print(f"SUCCESS: Cloud Payload synced at {sync_path}")
    
    print("\\n" + "="*40 + "\\nINTELLIGENT SYSTEM SYNC COMPLETE\\n" + "="*40)

if __name__ == "__main__":
    main()
""".strip()

# Create all files
for filepath, content in files.items():
    target_path = base_dir / filepath
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)

print("\\nProject 3: LabOps-Sync setup ready on your LENOVO!")
