import unittest

from color_code import name_color


class NameColorTests(unittest.TestCase):
    def test_black_color(self):
        code = "#000000"
        result = name_color(code)
        self.assertEqual(result, "black")

    def test_white_color(self):
        code = "#FFFFFF"
        result = name_color(code)
        self.assertEqual(result, "white")

    def test_red_color(self):
        code = "#FF0000"
        result = name_color(code)
        self.assertEqual(result, "red")

    def test_green_color(self):
        code = "#00FF00"
        result = name_color(code)
        self.assertEqual(result, "green")

    def test_blue_color(self):
        code = "#0000FF"
        result = name_color(code)
        self.assertEqual(result, "blue")

    def test_magenta_color(self):
        code = "#FF00FF"
        result = name_color(code)
        self.assertEqual(result, "magenta")

    def test_yellow_color(self):
        code = "#FFFF00"
        result = name_color(code)
        self.assertEqual(result, "yellow")

    def test_cyan_color(self):
        code = "#00FFFF"
        result = name_color(code)
        self.assertEqual(result, "cyan")

    def test_grey_color(self):
        code = "#888888"
        result = name_color(code)
        self.assertEqual(result, "grey")


if __name__ == "__main__":
    unittest.main()
