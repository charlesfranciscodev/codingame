import unittest

# Dictionary to cache already computed Fibonacci values
fib_cache = {}


def extended_fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n > 1:
        result = extended_fibonacci(n - 1) + extended_fibonacci(n - 2)
    else:  # n is negative
        result = extended_fibonacci(n + 2) - extended_fibonacci(n + 1)

    fib_cache[n] = result
    return result


class TestExtendedFibonacci(unittest.TestCase):
    def test_positive_index(self):
        self.assertEqual(extended_fibonacci(4), 3)

    def test_negative_index(self):
        self.assertEqual(extended_fibonacci(-4), -3)

    def test_zero_index(self):
        self.assertEqual(extended_fibonacci(0), 0)

    def test_caching(self):
        # Check if caching is working by computing the value for 5 twice
        # The second time, it should use the cached value
        extended_fibonacci(5)
        self.assertTrue(5 in fib_cache)

        result = extended_fibonacci(5)
        self.assertEqual(result, fib_cache[5])


if __name__ == "__main__":
    unittest.main()
