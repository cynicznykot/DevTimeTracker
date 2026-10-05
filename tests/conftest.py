"""
Pytest configuration.

Adds project root to sys.path for imports.
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))