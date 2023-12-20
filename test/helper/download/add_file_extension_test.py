from browserist import helper_download


def test_helper_download_add_file_extension() -> None:
    assert helper_download.add_file_extension("file.txt", ".download") == "file.txt.download"
