from browserist import helper_download


def test_helper_download_remove_file_extension() -> None:
    assert helper_download.remove_file_extension("file.txt.download", ".download") == "file.txt"
