from pathlib import Path

from browserist.helper.directory import operating_system
from browserist.model.type.path import FilePath

VALID_FILE_PATH = FilePath(Path.cwd())

VALID_ROOT_DIR_AS_STRING = "C:\\" if operating_system.is_windows() else "/"

VALID_PATH = Path(VALID_ROOT_DIR_AS_STRING)
