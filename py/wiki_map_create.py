import os
import re

def normalize_zone_name(zone_name):
    if zone_name.lower().startswith("the "):
        zone_name = zone_name[3:]
    elif zone_name.startswith("The "):
        zone_name = zone_name[4:]
    zone_name = zone_name.strip()
    words = zone_name.split()
    normalized_words = [word.capitalize() if word.lower() not in {"the", "of", "and"} else word for word in words]
    return ' '.join(normalized_words)

def create_markdown_link(zone_name):
    normalized_name = normalize_zone_name(zone_name)
    return f"[{normalized_name}](https://github.com/jedimud/jtin/wiki/Zone:-{normalized_name.replace(' ', '-')})"

def get_zone_names(directory_path):
    file_list = os.listdir(directory_path)
    zones_list = []
    for filename in file_list:
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            zone_name, _ = os.path.splitext(os.path.basename(filename))
            zone_name = normalize_zone_name(zone_name)
            zones_list.append({"zone_name": zone_name, "filename": filename})
    return zones_list

def create_zone_files(zones_list, target_path):
    for zone_info in sorted(zones_list, key=lambda x: x["zone_name"]):
        zone_name = zone_info["zone_name"]
        template_path = os.path.join("./templates", f"{zone_name}.md")
        if os.path.isfile(template_path):
            with open(template_path, 'r') as template_file:
                file_content = template_file.read()
        else:
            file_content = "No description\n"

        file_name = f"Zone: {zone_name}.md"
        file_path = os.path.join(target_path, file_name.replace(" ", "-"))
        with open(file_path, 'w') as file:
            file.write(file_content)

def get_connected_zones(filename):
    connected_zones = set()
    with open(filename, 'r') as file:
        for line in file:
            if "jt_m_link_action" in line:
                tokens = re.findall(r'{(.*?)}', line)
                if len(tokens) >= 4:
                    connected_zone = tokens[3].strip()

                    # Check if the filename contains " - "
                    if " - " not in connected_zone:
                        # Create Markdown link for each connected zone
                        markdown_link = create_markdown_link(connected_zone)
                        connected_zones.add(markdown_link)

    # Convert the set to a sorted list before returning
    return sorted(connected_zones)

def append_connected_zones(zones_list, target_path):
    for zone_info in zones_list:
        zone_name = zone_info["zone_name"]
        file_name = f"Zone: {zone_name}.md"
        file_path = os.path.join(target_path, file_name.replace(" ", "-"))

        connected_zones = get_connected_zones(os.path.join("./maps", zone_info["filename"]))
        
        with open(file_path, 'a') as file:
            file.write("\n## Connected Zones\n\n")
            for connected_zone in connected_zones:
                file.write(f"- {connected_zone}\n")

def filter_child_zones(zone_list):
    filtered_zones = [zone for zone in zone_list if " - " not in zone["zone_name"]]
    return filtered_zones

def main(directory_path, target_path):
    os.makedirs(target_path, exist_ok=True)

    zones_list = get_zone_names(directory_path)
    filtered_zones = filter_child_zones(zones_list)

    create_zone_files(filtered_zones, target_path)
    append_connected_zones(filtered_zones, target_path)

if __name__ == "__main__":
    directory_path = "./maps"
    target_path = "../jtin.wiki/zones"
    main(directory_path, target_path)
