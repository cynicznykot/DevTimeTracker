"""
Data models for the time tracker.

This module defines the core data structures used throughout the application.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Session:
    # Represents a single work session in a code editor.

    editor: str
    # Name of the editor (e.g., 'PyCharm', "VS Code").

    language: Optional[str]
    # Programming language detected from the file extension.

    file_path: Optional[str]
    # Path to the file being edited.

    start_time: datetime
    # Timestamp when the session started.

    end_time: Optional[datetime] = None
    # Timestamp when the session ended (None if still active).

    def get_duration(self):
        """
        Calculate the duration of the session in seconds.

        Returns:
            int: Duration in seconds. If session is active,
            calculates time from start to now.
        """
        end = self.end_time or datetime.now()
        return int((end - self.start_time).total_seconds())

