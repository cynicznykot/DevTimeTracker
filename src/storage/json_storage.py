import json
import os
from datetime import datetime
from typing import Dict


class JsonStorage:
    def __init__(self, file_path: str = "sessions.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump({"daily_stats": {}}, f, indent=2, ensure_ascii=False)

    def _save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_all(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"daily_stats": {}}

    def add_time(self, date: str, editor: str, seconds: int):
        data = self.load_all()

        if date not in data['daily_stats']:
            data['daily_stats'][date] = {}

        if editor not in data['daily_stats'][date]:
            data['daily_stats'][date][editor] = 0

        data['daily_stats'][date][editor] += seconds
        self._save_data(data)

    def get_daily_stats(self, date: str) -> Dict[str, int]:
        data = self.load_all()
        return data.get('daily_stats', {}).get(date, {})

    def get_total_time(self) -> int:
        data = self.load_all()
        total = 0
        for day in data.get('daily_stats', {}).values():
            total += sum(day.values())
        return total