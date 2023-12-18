import json
import os

def normalize_zone_name(zone_name):
    if zone_name.lower().startswith("the "):
        zone_name = zone_name[3:]
    elif zone_name.startswith("The "):
        zone_name = zone_name[4:]
    zone_name = zone_name.strip()
    words = zone_name.split()
    normalized_words = [word.capitalize() if word.lower() not in {"the", "of", "and"} else word for word in words]
    return ' '.join(normalized_words)

def create_npc_file(npc_name, kill_logs, loot_data):
    if npc_name.lower() != ",vendor":
        filename = f"../jtin.wiki/npcs/NPC:-{npc_name.replace(' ', '-').replace('_', ',')}.md"
        with open(filename, "w") as file:
            write_kill_log(file, kill_logs)
            write_loot_log(file, loot_data, npc_name)

def write_kill_log(file, kill_logs):
    file.write("## Kill Log\n\n")
    file.write("| Zone | Room | Count |\n")
    file.write("| :--- | :--- | ----: |\n")
    for log in kill_logs:
        normalized_zone = normalize_zone_name(log['zone'])
        zone_link = f"[{normalized_zone}](https://github.com/jedimud/jtin/wiki/Zone:-{normalized_zone.replace(' ', '-')})"
        room_info = f"{log['room_num']} - {log['room_name']}" 
        file.write(f"| {zone_link} | {room_info} | {log['kill_count']} |\n")

    file.write("\n")

def write_loot_log(file, loot_data, npc_name):
    file.write("## Loot Log\n\n")
    file.write("| Item | Zone | Room | Count |\n")
    file.write("| ---- | :--- | :--- | ----: |\n")

    loot_entries = loot_data.get(npc_name, [])

    for loot in loot_entries:
        if not isinstance(loot, dict):
            # Skip entries that are not dictionaries
            continue

        normalized_zone = normalize_zone_name(loot.get('zone', ''))
        zone_link = f"[{normalized_zone}](https://github.com/jedimud/jtin/wiki/Zone:-{normalized_zone.replace(' ', '-')})"
        room_info = f"{loot.get('room_num', '')} - {loot.get('room_name', '')}"
        file.write(f"| {loot.get('item', '')} | {zone_link} | {room_info} | {loot.get('loot_count', '')} |\n")

    file.write("\n")

def main():
    kill_log_path = "./data/wiki-npc-kill-briefs.json"
    loot_log_path = "./data/wiki-npc-loot-briefs.json"
    output_dir = "../jtin.wiki/npcs"

    os.makedirs(output_dir, exist_ok=True)

    with open(kill_log_path, "r") as kill_log_file:
        kill_data = json.load(kill_log_file)

    with open(loot_log_path, "r") as loot_log_file:
        loot_data = json.load(loot_log_file)

    for npc_name, kill_logs in kill_data.items():
        create_npc_file(npc_name, kill_logs, loot_data)

if __name__ == "__main__":
    main()