"""
Pytest configuration.

Adds project root to sys.path for imports.
"""

import sys
from pathlib import Path

# Project root = parent of tests/ directory
project_root = Path(__file__).parent.parent

# Add to sys.path if it exists
if project_root.exists():
    sys.path.insert(0, str(project_root))