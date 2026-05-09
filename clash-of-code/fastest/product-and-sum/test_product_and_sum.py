import unittest

from product_and_sum import product_and_sum_of_consecutive_integers


class TestProductAndSum(unittest.TestCase):
    def test_product_and_sum_positive(self):
        with self.subTest():
            self.assertEqual(product_and_sum_of_consecutive_integers(1), (1, 1))
            self.assertEqual(product_and_sum_of_consecutive_integers(2), (2, 3))
            self.assertEqual(product_and_sum_of_consecutive_integers(3), (6, 6))
            self.assertEqual(product_and_sum_of_consecutive_integers(4), (24, 10))
            self.assertEqual(product_and_sum_of_consecutive_integers(5), (120, 15))
        with self.subTest():
            self.assertEqual(product_and_sum_of_consecutive_integers(10), (3628800, 55))
        with self.subTest():
            self.assertEqual(product_and_sum_of_consecutive_integers(15), (1307674368000, 120))


if __name__ == "__main__":
    unittest.main()
