import json
import os
from datetime import datetime
from typing import List, Optional
from dataclasses import asdict

from src.core.tracker import Session

class JsonStorage:
    def __init__(self, file_path: str = "sessions.json"):
        self.file_path = file_path
        self._ensure_file_exists()
    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump({"sessions": []}, f, indent=2, ensure_ascii=False)

    def _save_data(self, data):
        with open(self.file_path, 'w', encoding='uft-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_all(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"sessions": []}

    def save_session(self, sessions: List):
        data = self.load_all()

        for session in sessions:
            session_dict = asdict(session)
            session_dict['start_time'] = session_dict['start_time'].isoformat()
            if session_dict['end_time']:
                session_dict['end_time'] = session_dict['end_time'].isoformat()
            data['sessions'].append(session_dict)

        self._save_data(data)