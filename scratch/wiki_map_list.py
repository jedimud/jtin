import os

def capitalize_except_specific_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() if word.lower() not in {"the", "of", "and"} else word for word in words]
    return ' '.join(capitalized_words)

def key_exists(key, dictionary):
    key_parts = key.split()
    for i in range(1, len(key_parts) + 1):
        partial_key = ' '.join(key_parts[:i])
        for existing_key in dictionary:
            if partial_key == existing_key and " - " in key:
                return True, partial_key
    return False, None

def assign_status(directory, filename):
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'r') as file:
        lines_containing_r = [line for line in file if "R {" in line]
        lines_containing_r_and_eva = [line for line in lines_containing_r if "<efa>" in line]

    count_total_rooms = len(lines_containing_r)
    count_unmapped_rooms = len(lines_containing_r_and_eva)

    ratio = 1.0 if count_unmapped_rooms == 0 else count_unmapped_rooms / count_total_rooms

    if ratio == 1.0:
        return ":white_check_mark:"
    elif 0.25 < ratio < 1.0:
        return ":link:"
    else:
        return ":o:"

def get_files_in_directory(directory):
    files_dict = {}

    # Get a list of files sorted by filename length
    file_list = sorted(os.listdir(directory), key=lambda x: len(x))

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            zone_name, _ = os.path.splitext(os.path.basename(filename))
            if zone_name.lower().startswith("the "):
                zone_name = zone_name[3:]
            elif zone_name.startswith("The "):
                zone_name = zone_name[4:]
            zone_name = zone_name.strip()
            zone_name = capitalize_except_specific_words(zone_name)

            exists, partial_key = key_exists(zone_name, files_dict)

            file_info = {
                "zone_name": zone_name,  # Include zone_name in the file_info dictionary
                "file_name": filename,
                "status": assign_status(directory, filename),
                "child_zones": {}
            }

            if not exists:
                if zone_name not in files_dict:
                    files_dict[zone_name] = []

                files_dict[zone_name].append(file_info)
            else:
                existing_file = files_dict[partial_key][0]
                if zone_name not in existing_file["child_zones"]:
                    existing_file["child_zones"][zone_name] = []

                existing_file["child_zones"][zone_name].append(file_info)

    return files_dict

def main(files_dict):
    print("| Zone | Map | Status |")
    print("| :--- | :-- | :----- |")

    def get_child_info(file_info):
        if "child_zones" not in file_info:
            return []

        child_info = []
        for child_zone_name, child_file_list in sorted(file_info["child_zones"].items()):
            for child_file_info in child_file_list:
                child_info.append({
                    "zone_name": child_zone_name,
                    "file_name": child_file_info["file_name"],
                    "status": child_file_info["status"]
                })

        return child_info

    for zone_name, file_list in sorted(files_dict.items()):
        for file_info in file_list:
            main_zone_name = file_info["zone_name"]
            main_file_name = f"`{file_info['file_name']}`"
            main_status = file_info["status"]

            child_info = get_child_info(file_info)

            if child_info:
                child_map_info = [
                    "`{}`".format(child["file_name"]) for child in child_info
                ]
                file_name = main_file_name + " <br> " + " <br> ".join(child_map_info)
                status = main_status + " <br> " + " <br> ".join(child["status"] for child in child_info)

                # Only print the parent zone once
                print('| {} | {} | {} |'.format(main_zone_name if child_info else main_zone_name,
                                                file_name, status))
            else:
                print('| {} | {} | {} |'.format(main_zone_name, main_file_name, main_status))


if __name__ == "__main__":
    files_dict = get_files_in_directory('./maps')
    main(files_dict)



