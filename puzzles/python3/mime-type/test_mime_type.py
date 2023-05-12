from unittest.mock import patch, call

from mime_type import main


def test_mime_type():
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
            main()

    # Assert
    mocked_print.assert_has_calls([call(output) for output in expected_output])


test_mime_type()
