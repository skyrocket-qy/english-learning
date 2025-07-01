import csv
from collections import defaultdict

input_file = 'total_words.csv'
output_file = 'total_words.csv'

merged_dict = defaultdict(set)

# Read and process CSV
with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        key = (row["word"], row["part_of_speech"])
        translations = [t.strip() for t in row["translate"].split(";")]
        merged_dict[key].update(translations)

# Prepare merged data
merged_data = [
    {
        "word": word,
        "part_of_speech": pos,
        "translate": ";".join(sorted(translations))
    }
    for (word, pos), translations in merged_dict.items()
]

# Write back to CSV
with open(output_file, 'w', encoding='utf-8', newline='') as file:
    fieldnames = ["word", "part_of_speech", "translate"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(merged_data)

print(f"Merged entries written: {len(merged_data)}")
