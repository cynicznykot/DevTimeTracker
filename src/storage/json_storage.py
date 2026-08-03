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
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_all(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"sessions": []}

    def save_session(self, session):
        data = self.load_all()

        session_dict = asdict(session)
        session_dict['start_time'] = session_dict['start_time'].isoformat()
        if session_dict['end_time']:
            session_dict['end_time'] = session_dict['end_time'].isoformat()

        data['sessions'].append(session_dict)
        self._save_data(data)

    def save_sessions(self, sessions):
        data = self.load_all()

        for session in sessions:
            session_dict = asdict(session)
            session_dict['start_time'] = session_dict['start_time'].isoformat()
            if session_dict['end_time']:
                session_dict['end_time'] = session_dict['end_time'].isoformat()
            data['sessions'].append(session_dict)

        self._save_data(data)

    def load_sessions(self):
        data = self.load_all()
        sessions = []

        for session_data in data.get('sessions', []):
            try:
                start_time = datetime.fromisoformat(session_data['start_time'])
                end_time = None
                if session_data.get('end_time'):
                    end_time = datetime.fromisoformat(session_data['end_time'])

                session = Session(
                    editor=session_data['editor'],
                    language=session_data['language'],
                    file_path=session_data['file_path'],
                    start_time=start_time,
                    end_time=end_time
                )
                sessions.append(session)
            except (KeyError, ValueError) as e:
                print(f"⚠️ Load Session error: {e}")
                continue

        return sessions

    def clear(self):
        self._save_data({"sessions": []})
