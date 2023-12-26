import json
import os

def read_json_file(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def create_item_files(data, target_path):
    for item_name in data.keys():
        # Create Markdown file path
        file_name = f"Item:-{item_name}.md"
        file_path = os.path.join(target_path, file_name)

        # Write "placeholder" content to the file
        with open(file_path, 'w') as item_file:
            item_file.write("placeholder")

def append_details(file_handle, data):
    ml = data.get("description", {}).get("ml", "")
    rests = data.get("description", {}).get("rests", "")
    affects = data.get("description", {}).get("affects", "")
    item_type = data.get("description", {}).get("type", "")
    spells = data.get("description", {}).get("spells", "")

    table_header = "| ML | Rests | Affects | Type | Spells |"
    table_alignment = "| -: | :---- | :------ | :--- | :----- |"
    table_line = f"| {ml} | {'`' + rests + '`' if rests else ''} | {'`' + affects + '`' if affects else ''} | {'`' + item_type + '`' if item_type else ''} | {'`' + spells + '`' if spells else ''} |"

    if any(detail.strip() for detail in [ml, rests, affects, item_type, spells]):
        file_handle.write(f"## Details\n{table_header}\n{table_alignment}\n{table_line}")

def append_tag_line(file_handle, data):
    tag = data.get("description", {}).get("tag", "")
    if tag:
        file_handle.write(f"\n\n## Tag Line\n`{tag}`")

def append_sac_line(file_handle, data):
    sac_line = data.get("description", {}).get("sac", "")
    if sac_line:
        file_handle.write(f"\n\n## Sac Line\n`{sac_line}`")

def append_loot_log(file_handle, loot_log):
    file_handle.write(f"\n\n## Loot Log\n{loot_log}")

def main(json_file_path, target_path):
    # Ensure the target directory exists
    os.makedirs(target_path, exist_ok=True)

    data = read_json_file(json_file_path)

    for item_name, item_data in data.items():
        # Replace spaces with dashes in the item name
        item_name_formatted = item_name.replace(" ", "-")

        # Create Markdown file path
        file_name = f"Item:-{item_name_formatted}.md"
        file_path = os.path.join(target_path, file_name)

        # Write content to the file
        with open(file_path, 'w') as item_file:
            append_details(item_file, item_data)
            append_tag_line(item_file, item_data)
            append_sac_line(item_file, item_data)
            append_loot_log(item_file, "Loot Log Placeholder")

if __name__ == "__main__":
    json_file_path = "./data/wiki-item-briefs.json"
    target_path = "../jtin.wiki/items"
    
    main(json_file_path, target_path)
