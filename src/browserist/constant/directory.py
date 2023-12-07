import os
from pathlib import Path

PROJECT_WORKING_DIR: Path = Path(__file__).parent.parent.parent.parent

USER_DIR = Path.home()

DOWNLOADS_DIR = os.path.join(USER_DIR, "Downloads")
