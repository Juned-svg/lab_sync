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
    
    print("\n" + "="*40 + "\nINTELLIGENT SYSTEM SYNC COMPLETE\n" + "="*40)

if __name__ == "__main__":
    main()