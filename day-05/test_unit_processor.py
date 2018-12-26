import unittest
from unit_processor import UnitProcessor


class TestUnitProcesser(unittest.TestCase):

    def test_should_collapse_single_unit_correctly(self):
        unit_processor = UnitProcessor()

        result = unit_processor.process("aA")

        self.assertEqual(result, "")

    def test_single_unit_should_be_collapsed_correctly_regardless_of_case_order(self):
        unit_processor = UnitProcessor()

        result = unit_processor.process("Aa")

        self.assertEqual(result, "")

    def test_ineligble_combinations_should_be_ignored(self):
        unit_processor = UnitProcessor()

        result = unit_processor.process("Ab")

        self.assertEqual(result, "Ab")

    def test_units_should_be_collapsed_recursively(self):
        unit_processor = UnitProcessor()

        result = unit_processor.process("ABba")

        self.assertEqual(result, "")

    def test_a_mix_of_collapsible_and_noncollapsible_units_should_be_handled_correctly(self):
        unit_processor = UnitProcessor()

        result = unit_processor.process("ABbaCDfeEFg")

        self.assertEqual(result, "CDg")


if __name__ == "__main__":
    unittest.main()
