# Open the file in read mode
file_path = 'scratch/rooms.txt'  # Replace with the actual file path
with open(file_path, 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# # Extract all integer values after "Zone:"
#     for line in lines:
#         if 'Zone:' in line:
#             print(line.strip())

    zone_values = set([int(line.split("[")[1].split("]")[0]) for line in lines if 'Zone:' in line])

# # Print or do something with the extracted values
    for zone_value in zone_values:
        print(zone_value)

import os

# Specify the folder path
folder_path = '/path/to/your/folder'  # Replace with the actual folder path

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Print the list of files
for file in file_list:
    print(file)