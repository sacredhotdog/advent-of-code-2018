_SINGLE_UNIT_WIDTH = 1
_DOUBLE_UNIT_WIDTH = 2


class UnitProcessor:

    def __init__(self):
        self._current_index = 0

    def process(self, polymer):
        should_process = True

        while should_process:
            reactive_units_present = False

            for index in range(len(polymer)):
                if index + 1 < len(polymer):
                    unit = polymer[index]
                    next_unit = polymer[index + _SINGLE_UNIT_WIDTH]

                    if self.meets_case_conditions(unit, next_unit) and self.match_ignoring_case(unit, next_unit):
                        polymer = self.remove_reactive_unit_pair(polymer, index)
                        reactive_units_present = True
                    else:
                        self._current_index += _SINGLE_UNIT_WIDTH

            should_process = reactive_units_present

        return polymer

    @staticmethod
    def meets_case_conditions(current_unit, next_unit):
        return (current_unit.islower() and next_unit.isupper()) or (current_unit.isupper() and next_unit.islower())

    @staticmethod
    def match_ignoring_case(current_unit, next_unit):
        return current_unit.upper() == next_unit.upper()

    @staticmethod
    def remove_reactive_unit_pair(polymer, current_position):
        return polymer[:current_position] + polymer[current_position + _DOUBLE_UNIT_WIDTH:]


if __name__ == "__main__":
    with open("polymer.txt") as file_object:
        polymer_data = file_object.read().strip()

        print(" -> Initial polymer length = " + str(len(polymer_data)))
        unit_processor = UnitProcessor()
        result = unit_processor.process(polymer_data)

    print(" -> Processed polymer length = " + str(len(result)))
    print(" -> Result: " + result)
