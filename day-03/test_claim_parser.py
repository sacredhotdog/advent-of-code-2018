import unittest
from claim_parser import ClaimParser


class TestClaimParser(unittest.TestCase):

    def test_empty_string_is_ignored(self):
        claim_parser = ClaimParser()

        result = claim_parser.parse("")

        self.assertIsNone(result)

    def test_none_is_ignored(self):
        claim_parser = ClaimParser()

        result = claim_parser.parse(None)

        self.assertIsNone(result)

    def test_whitespace_only_is_ignored(self):
        claim_parser = ClaimParser()

        result = claim_parser.parse(" ")

        self.assertIsNone(result)

    def test_handles_invalid_input(self):
        claim_input = "wqert123a ads"
        claim_parser = ClaimParser()

        result = claim_parser.parse(claim_input)

        self.assertIsNone(result)

    def test_claim_parsed_correctly(self):
        claim_input = "#1 @ 306,433: 16x11"
        claim_parser = ClaimParser()

        claim = claim_parser.parse(claim_input)

        self.assertEqual(claim.claim_id, 1)
        self.assertEqual(claim.inches_from_left_edge, 306)
        self.assertEqual(claim.inches_from_top_edge, 433)
        self.assertEqual(claim.width, 16)
        self.assertEqual(claim.height, 11)


if __name__ == "__main__":
    unittest.main()
