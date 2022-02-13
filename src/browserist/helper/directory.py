import os
from ..constant import directory

def create_if_not_exists(dir_name: str) -> None:
    if dir_name == directory.CURRENT:
        return
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def ensure_trailing_slash(dir_name: str) -> str:
    return dir_name if dir_name[-1] == "/" else f"{dir_name}/"
