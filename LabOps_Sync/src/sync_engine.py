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