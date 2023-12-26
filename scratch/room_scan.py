import os

directory = "./rooms"

# Use list comprehension to get a list of all .txt files in the specified directory and its subdirectories
files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if f.endswith(".txt")]

# Create a set to store the numeric parts of the file names
file_exists = set()

# Iterate over the files and populate the set
for file in files:
    number = ''.join(char for char in os.path.basename(file) if char.isdigit())
    file_exists.add(number)

# Iterate over the expected range (1-10) and check for the first missing file
for i in range(300, 10000):
    if str(i) not in file_exists:
        print(i)
        exit()

print("None")
