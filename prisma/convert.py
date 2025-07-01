import json
import csv

def json_dict_to_array(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    array = [[item['word'], item['part_of_speech'], item['translate']] for item in data]
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(array, f, ensure_ascii=False, indent=2)

# Converts dict JSON to array of arrays
# Export array of arrays JSON to CSV or TSV
def export_to_csv(input_file, output_file, delimiter=','):
    with open(input_file, 'r', encoding='utf-8') as f:
        array = json.load(f)
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(['word', 'part_of_speech', 'translate'])  # header
        writer.writerows(array)


        
if __name__ == '__main__':
    json_dict_to_array('total_words.json', 'words_array.json')
    export_to_csv('words_array.json', 'total_words.csv')