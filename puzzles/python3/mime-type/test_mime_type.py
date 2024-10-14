from unittest.mock import patch, call

from mime_type import mime_type_puzzle


def test_mime_type_with_unknown_extension():
    # Set up
    input_data = [
        "3",  # Number of elements
        "4",  # Number of names
        "txt text/plain",  # Extension and mime type mapping
        "jpg image/jpeg",  # Extension and mime type mapping
        "png image/png",  # Extension and mime type mapping
        "file.txt",  # Input name
        "image.jpg",  # Input name
        "file.doc",  # Input name with unknown extension
        "image.bmp",  # Input name with unknown extension
    ]
    expected_output = [
        "text/plain",  # Expected output for file.txt
        "image/jpeg",  # Expected output for image.jpg
        "UNKNOWN",  # Expected output for file.doc
        "UNKNOWN",  # Expected output for image.bmp
    ]

    # Execute
    with patch("builtins.input", side_effect=input_data):
        with patch("builtins.print") as mocked_print:
            mime_type_puzzle()

    # Assert
    mocked_print.assert_has_calls([call(output) for output in expected_output])


def test_mime_type_with_no_extension_or_dot_character():
    # Set up
    input_data = [
        "3",  # Number of elements
        "4",  # Number of names
        "html text/html",  # Extension and mime type mapping
        "png image/png",  # Extension and mime type mapping
        "gif image/gif",  # Extension and mime type mapping
        "file",  # Input name
        "image",  # Input name
        "file.",  # Input name with no extension
        "image.",  # Input name with no extension
    ]
    expected_output = [
        "UNKNOWN",
        "UNKNOWN",
        "UNKNOWN",
        "UNKNOWN",
    ]

    # Execute
    with patch("builtins.input", side_effect=input_data):
        with patch("builtins.print") as mocked_print:
            mime_type_puzzle()

    # Assert
    mocked_print.assert_has_calls([call(output) for output in expected_output])


def test_mime_type_with_different_cases():
    # Set up
    input_data = [
        "3",  # Number of elements
        "4",  # Number of names
        "txt text/plain",  # Extension and mime type mapping
        "jpg image/jpeg",  # Extension and mime type mapping
        "png image/png",  # Extension and mime type mapping
        "file.TXT",  # Input name
        "image.JPG",  # Input name
        "file.tXt",  # Input name
        "image.Png",  # Input name
    ]
    expected_output = [
        "text/plain",
        "image/jpeg",
        "text/plain",
        "image/png",
    ]

    # Execute
    with patch("builtins.input", side_effect=input_data):
        with patch("builtins.print") as mocked_print:
            mime_type_puzzle()

    # Assert
    mocked_print.assert_has_calls([call(output) for output in expected_output])


if __name__ == "__main__":
    test_mime_type_with_unknown_extension()
    test_mime_type_with_no_extension_or_dot_character()
    test_mime_type_with_different_cases()
