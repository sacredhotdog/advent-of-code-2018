from frequency_processor import FrequencyProcessor


class DuplicateFrequencyDetector:

    def __init__(self):
        self._frequency_processer = FrequencyProcessor()
        self._frequencies = {}
        self._duplicate_found = False
        self._duplicate_frequency = None

    def find_duplicates(self, frequency_input):
        while self.duplicate_found() is False:
            for line in frequency_input.split("\n"):
                if line is not None and len(line.replace(" ", "")) > 0:
                    self._frequency_processer.process(line)
                    self.record(self._frequency_processer.get_result())

    def record(self, frequency):
        if self.duplicate_found() is False:
            frequency_results = self._frequencies.get(frequency)

            if frequency_results is not None:
                self._frequencies[frequency] = frequency_results + 1
            else:
                self._frequencies[frequency] = 1

            if self._frequencies.get(frequency) > 1:
                self._duplicate_found = True
                self._duplicate_frequency = frequency

    def duplicate_found(self):
        return self._duplicate_found

    def get_duplicate(self):
        return self._duplicate_frequency


if __name__ == "__main__":
    file_name = "frequencies.txt"

    with open(file_name) as file_object:
        file_content = file_object.read()

    duplicate_frequency_detector = DuplicateFrequencyDetector()
    duplicate_frequency_detector.find_duplicates(file_content)

    print(" -> Duplicated frequency: " + str(duplicate_frequency_detector.get_duplicate()))
