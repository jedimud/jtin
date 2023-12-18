import pandas as pd
import json
from map_file_reader import MapFileReader

def aggregate_npc_kills(input_file, output_file, room_data_map):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file, header=None, names=['npc_name', 'zone', 'room_num'])
    except pd.errors.ParserError as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Rename columns to meaningful names
    df.columns = ['npc_name', 'zone', 'room_num']

    # Convert 'room_num' to integers
    df['room_num'] = pd.to_numeric(df['room_num'], errors='coerce', downcast='integer')

    # Drop rows with NaN values in 'room_num' (if any)
    df = df.dropna(subset=['room_num'])

    # Group by 'npc_name', 'zone', and 'room_num' and aggregate the counts
    aggregated_data = df.groupby(['npc_name', 'zone', 'room_num']).size().reset_index(name='kill_count')

    # Convert the DataFrame to a dictionary suitable for JSON
    result_dict = {}
    for index, row in aggregated_data.iterrows():
        npc_name = row['npc_name'].replace('_', ',')
        zone = row['zone']
        room_num = int(row['room_num'])
        kill_count = row['kill_count']

        # Get room_name using the preloaded room_data_map
        room_name = room_data_map[str(room_num)]['room_name']

        if npc_name not in result_dict:
            result_dict[npc_name] = []

        result_dict[npc_name].append({
            'zone': zone,
            'room_num': room_num,
            'room_name': room_name,
            'kill_count': kill_count
        })

    # Write the result to the specified JSON file path
    with open(output_file, 'w') as json_file:
        json.dump(result_dict, json_file, indent=2)

if __name__ == "__main__":
    map_reader = MapFileReader()
    room_data_map = map_reader.get_room_data_map()
    input_file = "./logs/loot.log"  # Modify input file path
    output_file = "./data/wiki-npc-kill-briefs.json"  # Modify output file path
    aggregate_npc_kills(input_file, output_file, room_data_map)