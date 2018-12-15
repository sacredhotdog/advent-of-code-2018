import unittest
from claim import Claim
from fabric import Fabric


class TestFabric(unittest.TestCase):

    def test_fabric_positions_default_to_zero(self):
        width = 2
        height = 3
        fabric = Fabric(width, height)

        for x in range(height):
            for y in range(width):
                self.assertEqual(fabric.get(x, y), 0)

    def test_place_single_claim(self):
        #       0   1   2
        #   +------------
        # 0 | 100 100   0
        # 1 | 100 100   0
        # 2 |   0   0   0

        claim = Claim(100, 0, 0, 2, 2)
        fabric_width = 3
        fabric_height = 3
        fabric = Fabric(fabric_width, fabric_height)

        fabric.place_claim(claim)

        self.assertEqual(fabric.get(0, 0), 100)
        self.assertEqual(fabric.get(0, 1), 100)
        self.assertEqual(fabric.get(0, 2), 0)
        self.assertEqual(fabric.get(1, 0), 100)
        self.assertEqual(fabric.get(1, 1), 100)
        self.assertEqual(fabric.get(1, 2), 0)
        self.assertEqual(fabric.get(2, 0), 0)
        self.assertEqual(fabric.get(2, 1), 0)
        self.assertEqual(fabric.get(2, 2), 0)

    def test_place_multiple_nonoverlapping_claims(self):
        #       0   1
        #   +--------
        # 0 | 100   0
        # 1 |   0 101

        claim1 = Claim(100, 0, 0, 1, 1)
        claim2 = Claim(101, 1, 1, 1, 1)
        fabric_width = 2
        fabric_height = 2
        fabric = Fabric(fabric_width, fabric_height)

        fabric.place_claim(claim1)
        fabric.place_claim(claim2)

        self.assertEqual(fabric.get(0, 0), 100)
        self.assertEqual(fabric.get(0, 1), 0)
        self.assertEqual(fabric.get(1, 0), 0)
        self.assertEqual(fabric.get(1, 1), 101)

    def test_duplicate_ids_are_ok(self):
        #       0   1
        #   +--------
        # 0 | 100   0
        # 1 |   0 100

        claim1 = Claim(100, 0, 0, 1, 1)
        claim2 = Claim(100, 1, 1, 1, 1)
        fabric_width = 2
        fabric_height = 2
        fabric = Fabric(fabric_width, fabric_height)

        fabric.place_claim(claim1)
        fabric.place_claim(claim2)

        self.assertEqual(fabric.get(0, 0), 100)
        self.assertEqual(fabric.get(0, 1), 0)
        self.assertEqual(fabric.get(1, 0), 0)
        self.assertEqual(fabric.get(1, 1), 100)

    def test_single_overlap_is_recorded_correctly(self):
        #       0   1   2
        #   +------------
        # 0 | 100 100   0
        # 1 | 100   X 101
        # 2 |   0 101 101

        claim1 = Claim(100, 0, 0, 2, 2)
        claim2 = Claim(101, 1, 1, 2, 2)
        fabric_width = 3
        fabric_height = 3
        fabric = Fabric(fabric_width, fabric_height)

        fabric.place_claim(claim1)
        fabric.place_claim(claim2)

        self.assertEqual(fabric.get(0, 0), 100)
        self.assertEqual(fabric.get(0, 1), 100)
        self.assertEqual(fabric.get(0, 2), 0)
        self.assertEqual(fabric.get(1, 0), 100)
        self.assertEqual(fabric.get(1, 1), "X")
        self.assertEqual(fabric.get(1, 2), 101)
        self.assertEqual(fabric.get(2, 0), 0)
        self.assertEqual(fabric.get(2, 1), 101)
        self.assertEqual(fabric.get(2, 2), 101)

    def test_multiple_overlap_is_recorded_correctly(self):
        #       0   1   2   3   4
        #   +--------------------
        # 0 | 100 100   0   0   0
        # 1 | 100   X 101 101   0
        # 2 |   0 101 101 101   0
        # 3 |   0   X   X   X   0
        # 4 |   0 102 102 102   0
        # 5 |   0   0   0   0   0

        claim1 = Claim(100, 0, 0, 2, 2)
        claim2 = Claim(101, 1, 1, 3, 3)
        claim3 = Claim(102, 1, 3, 3, 2)
        fabric_width = 5
        fabric_height = 6
        fabric = Fabric(fabric_width, fabric_height)

        fabric.place_claim(claim1)
        fabric.place_claim(claim2)
        fabric.place_claim(claim3)

        self.assertEqual(fabric.get(0, 0), 100)
        self.assertEqual(fabric.get(0, 1), 100)
        self.assertEqual(fabric.get(0, 2), 0)
        self.assertEqual(fabric.get(0, 3), 0)
        self.assertEqual(fabric.get(0, 4), 0)
        self.assertEqual(fabric.get(1, 0), 100)
        self.assertEqual(fabric.get(1, 1), "X")
        self.assertEqual(fabric.get(1, 2), 101)
        self.assertEqual(fabric.get(1, 3), 101)
        self.assertEqual(fabric.get(1, 4), 0)
        self.assertEqual(fabric.get(2, 0), 0)
        self.assertEqual(fabric.get(2, 1), 101)
        self.assertEqual(fabric.get(2, 2), 101)
        self.assertEqual(fabric.get(2, 3), 101)
        self.assertEqual(fabric.get(2, 4), 0)
        self.assertEqual(fabric.get(3, 0), 0)
        self.assertEqual(fabric.get(3, 1), "X")
        self.assertEqual(fabric.get(3, 2), "X")
        self.assertEqual(fabric.get(3, 3), "X")
        self.assertEqual(fabric.get(3, 4), 0)
        self.assertEqual(fabric.get(4, 0), 0)
        self.assertEqual(fabric.get(4, 1), 102)
        self.assertEqual(fabric.get(4, 2), 102)
        self.assertEqual(fabric.get(4, 3), 102)
        self.assertEqual(fabric.get(4, 4), 0)
        self.assertEqual(fabric.get(5, 0), 0)
        self.assertEqual(fabric.get(5, 1), 0)
        self.assertEqual(fabric.get(5, 2), 0)
        self.assertEqual(fabric.get(5, 3), 0)
        self.assertEqual(fabric.get(5, 4), 0)


if __name__ == "__main__":
    unittest.main()
