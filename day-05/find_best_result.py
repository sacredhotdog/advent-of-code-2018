from unit_processor import UnitProcessor
from collections import Counter


with open("polymer.txt") as file_object:
    polymer_data = file_object.read().strip()
    shortest_result = len(polymer_data)

    counter = Counter(polymer_data)
    unit_processor = UnitProcessor()
    processed = []
    count = 0

    print(" -> Preparing to process " + str(len(counter.keys())) + " keys...")

    for key in counter.keys():
        count += 1
        print(" -> Processing key '" + key + "' (" + str(count) + " of " + str(len(counter.keys())) + ")...")

        if key.upper() not in processed:
            revised_polymer = polymer_data.replace(key.upper(), "").replace(key.lower(), "")
            result = unit_processor.process(revised_polymer)
            processed.append(key.upper())
            result_length = len(result)

            if result_length < shortest_result:
                shortest_result = result_length

            print(" -> Shortest result so far: " + str(shortest_result))
        else:
            print("\tAlready processed, skipping...")

print(" -> Shortest processed polymer length = " + str(shortest_result))
print(" -> Result: " + str(shortest_result))
