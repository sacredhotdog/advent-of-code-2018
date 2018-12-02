_OPERATION_INDEX = 0


class FrequencyProcessor:

    def __init__(self):
        self._frequency = 0

    def get_result(self):
        return self._frequency

    def process(self, frequency_change):
        frequency_change = self.prepare_input(frequency_change)

        if frequency_change is not None:
            operator = frequency_change[_OPERATION_INDEX]

            try:
                frequency = int(frequency_change[_OPERATION_INDEX+1:])
                self.adjust_frequency(operator, frequency)
            except ValueError:
                print(" !! Yuck: " + str(frequency_change))

    def adjust_frequency(self, operator, frequency):
        if operator is "+":
            self._frequency += frequency
        elif operator is "-":
            self._frequency -= frequency

    def prepare_input(self, frequency_change):
        if frequency_change is not None:
            frequency_change = frequency_change.replace(" ", "")

            if len(frequency_change) > 0:
                return frequency_change.strip("\n")
            else:
                return None


if __name__ == "__main__":
    file_name = "frequencies.txt"
    frequency_processor = FrequencyProcessor()

    with open(file_name) as file_object:
        for line in file_object:
            frequency_processor.process(line)

    print(" -> Frequency = " + str(frequency_processor.get_result()))
