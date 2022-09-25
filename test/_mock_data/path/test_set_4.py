from pathlib import Path

from browserist.model.type.path import FilePath

VALID_FILE_PATH = FilePath(Path.cwd())

VALID_ROOT_DIR_AS_STRING = "/"

VALID_PATH = Path(VALID_ROOT_DIR_AS_STRING)
