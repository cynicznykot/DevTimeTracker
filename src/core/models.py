"""
Data models for the time tracker.

This module defines the core data structures used throughout the application.
"""


from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Session:
    """
    Represents a single work session in a code editor.

    Attributes:
        editor: Name of the editor (e.g., 'PyCharm', 'VS Code').
        language: Programming language detected from file extension.
        file_path: Path tot the file being edited.
        start_time: Timestamp when the session started.
        end_time: Timestamp when the sessions ended (None if active)
    """

    editor: str
    language: Optional[str]
    file_path: Optional[str]
    start_time: datetime
    end_time: Optional[datetime] = None

    def get_duration(self) -> int:
        """
        Calculate the duration of the session in seconds.

        Returns:
            int: Duration in seconds. If session is active,
            calculates time from start to now.
        """
        end = self.end_time or datetime.now()
        return int((end - self.start_time).total_seconds())

