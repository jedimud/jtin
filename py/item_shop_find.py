import re
import sys
import item_brief_find

def split_string(input_string):
    components = re.split(r'\s+', input_string.strip())
    
    components[0] = components[0].rjust(4)
    print(components[0] + ' ')

    if "Unlimited" in components[1]:
        components[1] = "Unl "
    else:
        components[1] = components[1].rjust(3) + ' '

    print(components[1])
    item_name = ' '.join(components[2:-1]).replace('_', "'")
    print(item_name)

    print(components[-1].rjust(7) + ' ')

    item_brief_find.find_item(item_name, "")

if __name__ == "__main__":
    split_string(sys.argv[1])