import glob

class MapFileReader:
    DIRECTORY_PATH = "./maps"

    def __init__(self):
        self.room_data_map = {}
        self.read_map_files()

    def read_map_files(self):
        # Get a list of file paths matching the pattern
        map_files = glob.glob(f"{self.DIRECTORY_PATH}/*.map")

        # Loop through each file
        for file_path in map_files:
            with open(file_path, 'r') as file:
                # Read lines from the file
                lines = file.readlines()

                # Process lines
                for line in lines:
                    if "R {" in line:
                        # Split the line into tokens using curly braces
                        tokens = line.split('{')

                        # Extract relevant information
                        room_number = tokens[1].rstrip('}').strip()
                        room_name = tokens[4].split('}')[0].strip()
                        zone_name = tokens[7].split('}')[0].strip()

                        # Ignore lines where room name or zone name is null/empty
                        if room_name and zone_name:
                            # Store the extracted information in a dictionary
                            self.room_data_map[room_number] = {
                                'room_name': room_name,
                                'zone_name': zone_name
                            }

    def get_room_data_map(self):
        return self.room_data_map

if __name__ == "__main__":
    # Example usage:
    map_reader = MapFileReader()
    room_data_map = map_reader.get_room_data_map()

    # Print or process the entire room data map
    for room_number, room_data in room_data_map.items():
        print(f"Room Number: {room_number}, Room Name: {room_data['room_name']}, Zone Name: {room_data['zone_name']}")
