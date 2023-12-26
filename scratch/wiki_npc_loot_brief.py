import pandas as pd
import json
from map_file_reader import MapFileReader

def get_room_name(room_num, map_reader):
    room_data_map = map_reader.get_room_data_map()
    return room_data_map.get(room_num, {}).get('room_name', 'placeholder')

def aggregate_npc_loot(input_file, output_file, room_data_map):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file, header=None, names=['item', 'npc_name', 'zone', 'room_num'])
    except pd.errors.ParserError as e:
        print(f"Error reading CSV file: {e}")
        return

    # Drop rows where 'item' is null
    df = df.dropna(subset=['item'])

    # Group by 'npc_name', 'zone', 'room_num', and 'item' and aggregate the counts
    aggregated_data = df.groupby(['npc_name', 'zone', 'room_num', 'item']).size().reset_index(name='loot_count')

    # Convert the DataFrame to a dictionary suitable for JSON
    result_dict = {}
    for index, row in aggregated_data.iterrows():
        npc_name = row['npc_name'].replace('_', ',')
        zone = row['zone']
        room_num = row['room_num']
        item = row['item'].replace('_', ',')
        loot_count = row['loot_count']

        # Get room_name using the preloaded room_data_map
        room_name = room_data_map[str(room_num)]['room_name']

        if npc_name not in result_dict:
            result_dict[npc_name] = []

        result_dict[npc_name].append({
            'zone': zone,
            'room_num': room_num,
            'room_name': room_name,
            'item': item,
            'loot_count': loot_count
        })

    # Write the result to the specified JSON file path
    with open(output_file, 'w') as json_file:
        json.dump(result_dict, json_file, indent=2)

if __name__ == "__main__":
    map_reader = MapFileReader()
    room_data_map = map_reader.get_room_data_map()
    input_file = "./logs/loot.log"
    output_file = "./data/wiki-npc-loot-briefs.json"
    aggregate_npc_loot(input_file, output_file, room_data_map)
