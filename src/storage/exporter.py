"""
Data export module.

Provides functionality to export statistics to various formats.
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict

from src.storage.json_storage import JsonStorage


class DataExporter:
    """
    Export statistics to various formats.

    Supports:
    - CSV (for Excel, Google Sheets)
    - JSON (for backup, integration)
    """

    def __init__(self, storage: JsonStorage):
        """
        Initialize exporter.

        Args:
            storage: JsonStorage instance with data.
        """
        self.storage = storage

    def export_csv(self, file_path: str = "start_export.csv") -> bool:
        """
        Export statistics to CSV file.

        Args:
            file_path: Output file path.

        Returns:
            True if export was successful, False otherwise.
        """
        try:
            data = self.storage.load_all()
            daily_stats = data.get('daily_stats', {})

            if not daily_stats:
                print("📊 No data to export.")
                return False

            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Date', 'Editor', 'Seconds', 'Hours', 'Minutes'])

                for date, editors in sorted(daily_stats.items()):
                    for editor_name, seconds in editors.items():
                        hours = seconds // 3600
                        minutes = (seconds % 3600) // 60
                        writer.writerow([data, editor_name, seconds, hours, minutes])

            print(f"✅ Exported to {file_path}")
            return True

        except Exception as e:
            print(f"❌ Export error: {e}")
            return False

    def export_json(self, file_path: str = "stats_export.json") -> bool:
        """
        Export statistics to JSON file.

        Args:
            file_path: Output file path.

        Returns:
            True if export was successful, False otherwise.
        """
        try:
            data = self.storage.load_all()

            if not data.get('daily_stats'):
                print("📊 No data to export.")
                return False

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"✅ Exported to {file_path}")
            return True

        except Exception as e:
            print(f"❌ Export error: {e}")
            return False