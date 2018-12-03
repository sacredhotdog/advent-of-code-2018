import unittest
from claim import Claim


class TestClaim(unittest.TestCase):

    def test_defaults_should_be_correct(self):
        claim = Claim()

        self.assertIsNone(claim.claim_id)
        self.assertIsNone(claim.inches_from_left_edge)
        self.assertIsNone(claim.inches_from_top_edge)
        self.assertIsNone(claim.width)
        self.assertIsNone(claim.height)


if __name__ == "__main__":
    unittest.main()
