"""
JSON storage module for session persistence.

This module provides a simple JSON-based storage backend for saving
and loading time tracking statistics. Data is stored in a human-readable
JSON file with a structure optimized for daily statistics.

File structure:
    {
        "daily_stats": {
            "2026-08-07": {
                "PyCharm": 3600,
                "VS Code": 1800
            },
            "2026-08-06": {
                "PyCharmd":7200
            }
        }
    }

Example:
    >>> from src.storage.json_storage import JsonStorage
    >>> storage = JsonStorage()
    >>> storage.add_time("2026-08-07", "PyCharm", 3600)
    >>> stats = storage.get_daily_stats("2026-08-07")
    >>> print(stats)  # {'PyCharm': 3600}
"""

import json
import os
from datetime import datetime
from typing import Dict


class JsonStorage:
    """
    JSON-based storage for time tracking statistics.

    This class handles reading and writing statistics to a JSON file.
    Data is stored as daily stats per edition, allowing for easy querying
    and aggregation.

    Attributes:
        file_path (str): Path to the JSON file.
    """
    def __init__(self, file_path: str = "sessions.json"):
        """ Initialize the JSON storage.

        Args:
            file_path: Path to the JSON file. Default is 'sessions.json'
        """

        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """
        Create the JSON file with default structure if it doesn't exist.

        If the file doesn't exist, creates it with an empty daily_stats
        structure: {"daily_stats": {}}
        """

        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump({"daily_stats": {}}, f, indent=2, ensure_ascii=False)

    def _save_data(self, data: dict) -> None:
        """
        Save data to the JSON file.

        Args:
            data: Dictionary constaining the statistics data.
        """

        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_all(self) -> dict:
        """
        Load all data from the JSON file.

        Returns:
            Dictionary containing all statistics data.
            If file doesn't exist or is corrupted, returns {"daily_stats": {}}

        Example:
            >>> storage = JsonStorage()
            >>> data = storage.load_all()
            >>> data.keys()
            dict_keys(['daily_stats'])
        """

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"daily_stats": {}}

    def add_time(self, date: str, editor: str, seconds: int) -> None:
        """
        Add time ti the daily statistics for a specific editor.

        This method adds the specified seconds to the editor's total
        for the given date. If the date of editor doesn't exist,
        they are created automatically.

        Args:
            date: Date string in format 'YYYY-MM-DD'.
            editor: Name of the editor (e.g., 'PyCharm').
            seconds: Number of seconds to add.

        Example:
            >>> storage = JsonStorage()
            >>> storage.add_time("2026-08-07", "PyCharm", 3600)
            # Adds 1 hour of PyCharm time for today
        """

        data = self.load_all()

        if date not in data['daily_stats']:
            data['daily_stats'][date] = {}

        if editor not in data['daily_stats'][date]:
            data['daily_stats'][date][editor] = 0

        data['daily_stats'][date][editor] += seconds
        self._save_data(data)

    def get_daily_stats(self, date: str) -> Dict[str, int]:
        """
        Get statistics for a specific day.

        Args:
            date: Date string in format 'YYYY-MM-DD'

        Returns:
            Dictionary mapping editor names to total seconds for that date.
            Returns empty dict if date has no data.

        Example:
            >>> storage = JsonStorage()
            >>> stats = storage.get_daily_stats("2026-08-07")
            >>> stats
            {'PyCharm': 3600, 'VS Code':1800}
        """

        data = self.load_all()
        return data.get('daily_stats', {}).get(date, {})

    def get_all_stats(self) -> Dict[str, int]:
        """
        Get total statistics for all time, aggregated by editor.

        This method sums up all the spent in each editor across all dates.

        Returns:
            Dictionary mapping editor names to total seconds across all time.

        Example:
            >>> storage = JsonStorage()
            >>> stats = storage.get_all_stats()
            >>> stats{'PyCharm': 7200, 'VS Code': 5400}
        """

        data = self.load_all()
        total_stats = {}

        for day in data.get('daily_stats', {}).values():
            for editor, seconds in day.items():
                if editor not in total_stats:
                    total_stats[editor] = 0
                total_stats[editor] += seconds

        return total_stats