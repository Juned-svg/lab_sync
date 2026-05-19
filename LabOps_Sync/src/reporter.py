import pandas as pd
from datetime import datetime
from pathlib import Path

class LabReportGenerator:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        
    def generate_batch_report(self, batch_id, stats, anomalies):
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        status = "⚠️ INVESTIGATION REQUIRED" if anomalies > 0 else "✅ COMPLIANT"
        
        content = f"""
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
"""
        report_path = self.output_dir / f"Report_{batch_id}.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        return report_path