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

    def test_initialisation_should_be_correct(self):
        claim_id = 999
        inches_from_left = 1
        inches_from_top = 2
        width = 3
        height = 4

        claim = Claim(claim_id, inches_from_left, inches_from_top, width, height)

        self.assertEqual(claim.claim_id, claim_id)
        self.assertEqual(claim.inches_from_left_edge, inches_from_left)
        self.assertEqual(claim.inches_from_top_edge, inches_from_top)
        self.assertEqual(claim.width, width)
        self.assertEqual(claim.height, height)


if __name__ == "__main__":
    unittest.main()
