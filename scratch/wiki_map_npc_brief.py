import pandas as pd
import json
from map_file_reader import MapFileReader

def get_loot_data(loot_file):
    try:
        with open(loot_file, 'r') as json_file:
            loot_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading loot JSON file: {e}")
        return {}

    return loot_data

def group_npc_data(input_file, output_file, room_data_map, loot_file):
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

    # Exclude NPCs ending with "_vendor"
    df = df[~df['npc_name'].str.endswith('_vendor')]

    # Group by 'zone', 'npc_name', and 'room_num'
    grouped_data = df.groupby(['zone', 'npc_name', 'room_num']).size().reset_index(name='dummy_column')

    # Read loot data
    loot_data = get_loot_data(loot_file)

    # Convert loot data to a DataFrame
    loot_df = pd.DataFrame([(key, value) for key, values in loot_data.items() for value in values], columns=['npc_name', 'loot_info'])

    # Merge loot data with the existing grouped data
    merged_data = pd.merge(grouped_data, loot_df, on=['npc_name'], how='left')

    # Convert the merged DataFrame to a dictionary suitable for JSON
    result_dict = {}
    for index, row in merged_data.iterrows():
        npc_name = row['npc_name'].replace('_', ',')
        zone = row['zone']
        room_num = int(row['room_num'])
        room_name = room_data_map[str(room_num)]['room_name']
        loot_info = row['loot_info']

        if zone not in result_dict:
            result_dict[zone] = []

        # Set NaN values in 'loot' to null
        loot_info = loot_info if pd.notna(loot_info) else None

        result_dict[zone].append({
            'npc_name': npc_name,
            'room_num': room_num,
            'room_name': room_name,
            'loot': loot_info
        })

    # Sort the arrays within each 'zone' by 'npc_name' case-insensitively
    for zone in result_dict:
        result_dict[zone] = sorted(result_dict[zone], key=lambda x: x['npc_name'].lower())

    # Write the result to the specified JSON file path in the "./data" directory
    with open(output_file, 'w') as json_file:
        json.dump(result_dict, json_file, indent=2)

if __name__ == "__main__":
    map_reader = MapFileReader()
    room_data_map = map_reader.get_room_data_map()
    input_file = "./logs/loot.log"  # Modify input file path
    output_file = "./data/wiki_map_npc_briefs.json"  # Modify output file path
    loot_file = "./data/wiki-npc-loot-briefs.json"  # Modify loot file path
    group_npc_data(input_file, output_file, room_data_map, loot_file)
