import unittest

from power_of_thor1 import solve


class TestSolve(unittest.TestCase):
    def test_thor_above_light(self):
        light_x = 5
        light_y = 5
        thor_x = 5
        thor_y = 4
        expected_direction = "S"

        result_direction, result_thor_x, result_thor_y = solve(light_x, light_y, thor_x, thor_y)
        self.assertEqual(result_direction, expected_direction)
        self.assertEqual(result_thor_x, light_x)
        self.assertEqual(result_thor_y, light_y)

    def test_thor_below_light(self):
        light_x = 5
        light_y = 5
        thor_x = 5
        thor_y = 6
        expected_direction = "N"

        result_direction, result_thor_x, result_thor_y = solve(light_x, light_y, thor_x, thor_y)
        self.assertEqual(result_direction, expected_direction)
        self.assertEqual(result_thor_x, light_x)
        self.assertEqual(result_thor_y, light_y)

    def test_thor_left_of_light(self):
        light_x = 5
        light_y = 5
        thor_x = 4
        thor_y = 5
        expected_direction = "E"

        result_direction, result_thor_x, result_thor_y = solve(light_x, light_y, thor_x, thor_y)
        self.assertEqual(result_direction, expected_direction)
        self.assertEqual(result_thor_x, light_x)
        self.assertEqual(result_thor_y, light_y)

    def test_thor_right_of_light(self):
        light_x = 5
        light_y = 5
        thor_x = 6
        thor_y = 5
        expected_direction = "W"

        result_direction, result_thor_x, result_thor_y = solve(light_x, light_y, thor_x, thor_y)
        self.assertEqual(result_direction, expected_direction)
        self.assertEqual(result_thor_x, light_x)
        self.assertEqual(result_thor_y, light_y)

    def test_thor_several_cells_from_light(self):
        light_x = 5
        light_y = 5
        thor_x = 15
        thor_y = 5
        expected_direction = "W"
        expected_thor_x = 14

        result_direction, result_thor_x, result_thor_y = solve(light_x, light_y, thor_x, thor_y)
        self.assertEqual(result_direction, expected_direction)
        self.assertEqual(result_thor_x, expected_thor_x)
        self.assertEqual(result_thor_y, light_y)

    def test_diagonal_direction(self):
        light_x = 5
        light_y = 5
        thor_x = 15
        thor_y = 15
        expected_direction = "NW"
        expected_thor_x = 14
        expected_thor_y = 14

        result_direction, result_thor_x, result_thor_y = solve(light_x, light_y, thor_x, thor_y)
        self.assertEqual(result_direction, expected_direction)
        self.assertEqual(result_thor_x, expected_thor_x)
        self.assertEqual(result_thor_y, expected_thor_y)


if __name__ == "__main__":
    unittest.main()
