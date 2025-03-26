import json

def calc_eff(filepath):
# Load the JSON data from a file
    with open(filepath, 'r') as file:
        json_data = json.load(file)

    # Calculate the efficiency metric for each object
    for obj in json_data:
        obj['Efficiency_metric'] = (( obj['Num_Nodes'] + 1) * (obj['Num_edges'] + 1)) / obj['Num_tokens']

    #cutof top results
    data_sorted = sorted(json_data, key=lambda x: x.get('Efficiency_metric', 0), reverse=True)
    data_trimmed = data_sorted[1000:]
    json_data = data_trimmed
    # Find the object with the highest efficiency metric
    most_efficient_object = max(json_data, key=lambda x: x['Efficiency_metric'])
    max_efficiency_metric = most_efficient_object['Efficiency_metric']

    # Update efficiency values relative to the highest efficiency metric
    for obj in json_data:
        obj['Efficiency'] = obj['Efficiency_metric'] / max_efficiency_metric if max_efficiency_metric != 0 else 0

    # Ensure the most efficient object has an efficiency of exactly 1
    most_efficient_object['Efficiency'] = 1

    # Optionally, write the updated JSON to a new file
    with open('/home/a200161455/projects/WAB5_Lightrag/updated_data.json', 'w') as file:
        json.dump(json_data, file, indent=4)
    print(json_data[:10])
calc_eff("path to/output_wo_eff.json")
