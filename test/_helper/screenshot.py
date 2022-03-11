import os

MINIMUM_FILE_SIZE = 1000


def image_has_minimum_file_size(directory: str, file_name: str) -> bool:
    return os.path.getsize(f"{directory}/{file_name}") > MINIMUM_FILE_SIZE


def images_have_minimum_file_size(directory: str) -> bool:
    def absolute_path(file: str) -> str:
        return os.path.join(directory, file)

    files = [absolute_path(file) for file in os.listdir(directory) if os.path.isfile(absolute_path(file))]
    return all(os.path.getsize(file) > MINIMUM_FILE_SIZE for file in files)
