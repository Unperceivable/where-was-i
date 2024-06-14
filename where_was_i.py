import json
import argparse
import os
from collections import defaultdict

# Load Google Maps location history from all JSON files in the specified year folder
def load_location_history(year_folder):
    location_history = []
    for filename in os.listdir(year_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(year_folder, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                location_history.extend(data['timelineObjects'])
    return location_history

# Count visits to the target location in the specified year
def count_visits(location_history, semantic_type):
    visit_count = defaultdict(int)
    for location in location_history:
        location_type = list(location.keys())
        if "placeVisit" in location_type:
            place_locaction = location["placeVisit"]["location"]
            if place_locaction.get("semanticType") == semantic_type:
                visit_count[place_locaction["address"]] += 1

    return visit_count

def main():
    parser = argparse.ArgumentParser(description='Count visits to a specific location in a given year from Google Maps history.')
    parser.add_argument('year_folder', type=str, help='Path to the folder containing the location history JSON files for the specified year')
    parser.add_argument('--semantic_type', type=str, help='Semantic type of the location (e.g., TYPE_WORK, TYPE_HOME)', default='TYPE_WORK')

    args = parser.parse_args()
    
    location_history = load_location_history(args.year_folder)
    visit_count = count_visits(location_history, args.semantic_type)
    
    print(f"You visited the following {args.semantic_type} locations a total of {sum(visit_count.values())} times: {dict(visit_count)}")

if __name__ == "__main__":
    main()
