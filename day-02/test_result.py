import unittest
from result import Result


class TestResult(unittest.TestCase):

    def test_result_defaults_are_correct(self):
        result = Result()

        self.assertFalse(result.contains_duplicate)
        self.assertFalse(result.contains_triplicate)


if __name__ == "__main__":
    unittest.main()
