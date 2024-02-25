import unittest

from clash_royal import calculate_damage
from clash_royal import clash_royal_match


class TestClashRoyalMatch(unittest.TestCase):
    def test_damage_calculation(self):
        self.assertEqual(calculate_damage(1), 200)
        self.assertEqual(calculate_damage(5), 280)
        self.assertEqual(calculate_damage(10), 380)

    def test_clash_royal_match(self):
        # Test when health is greater than damage
        result, remaining_health = clash_royal_match(300, 1)
        self.assertEqual(result, "rawr")
        self.assertEqual(remaining_health, 100)

        # Test when health equals damage
        result, remaining_health = clash_royal_match(200, 1)
        self.assertEqual(result, "hehehehaw")
        self.assertEqual(remaining_health, 0)

        # Test when health is less than damage
        result, remaining_health = clash_royal_match(100, 10)
        self.assertEqual(result, "hehehehaw")
        self.assertEqual(remaining_health, -280)


if __name__ == "__main__":
    unittest.main()
