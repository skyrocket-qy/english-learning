import csv
import json

# Input and output file paths
csv_file = 'total_words.csv'
json_file = 'total_words.json'

# Define the field mapping from CSV to JSON
# Assumes your CSV header is: word,part_of_speech,translate
output = []

with open(csv_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        word = {
            'english': row['word'],
            'partOfSpeech': row['part_of_speech'],
            'chinese': row['translate'],
        }
        output.append(word)

# Write to JSON file
with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ Converted {len(output)} entries to {json_file}")
