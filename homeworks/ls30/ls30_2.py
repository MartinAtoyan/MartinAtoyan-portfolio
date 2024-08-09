import json


def filter_json_data_with_loop(input_file, output_file, filter_key, filter_value):
    file = open(input_file, 'r')
    data = json.load(file)
    filtered_data = []
    for entry in data:
        if entry.get(filter_key) == filter_value:
            filtered_data.append(entry)

    file = open(output_file, 'w')
    json.dump(filtered_data, file, indent=4)

    print(f"Filtered data has been written to {output_file}")
