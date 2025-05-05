import re

def map_phase(lines, target_word):
    mapped = []
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())  
        for word in words:
            if word == target_word.lower():
                mapped.append((target_word.lower(), 1))
    return mapped

def reduce_phase(mapped_data):
    reduced = {}
    for key, value in mapped_data:
        reduced[key] = reduced.get(key, 0) + value
    return reduced

# ------------ MAIN ------------ #

target_word = "hrugved"
file_name = "input.txt"

with open(file_name, 'r') as f:
    lines = f.readlines()

mapped_data = map_phase(lines, target_word)
reduced_result = reduce_phase(mapped_data)

for word, count in reduced_result.items():
    print(f"{word}\t{count}")
