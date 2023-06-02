from steganography import insert_info


def run_integration_tests():
    # Basic test case
    info = "110100101"
    image = [[122, 157, 223],
             [64, 125, 253],
             [128, 192, 168]]
    expected_output = [[123, 157, 222],
                       [65, 124, 252],
                       [129, 192, 169]]
    result = insert_info(info, image)
    assert result == expected_output, f"Test 1 failed: {result}"


if __name__ == "__main__":
    run_integration_tests()
