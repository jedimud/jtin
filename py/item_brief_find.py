import json
import sys
import os.path


def find_item(item_name, insure_tag):

    if not os.path.exists("data/item-briefs.json"):
        print(item_name)
        print()
        print()
        print()
        print(insure_tag)
        print()
        print()

        return

    with open("data/item-briefs.json") as f:
        data = json.load(f)

    item_name_lower = item_name.lower()
    if item_name_lower in data:
        print(item_name)
        print(data[item_name_lower]['description']['equipped'])
        print(data[item_name_lower]['description']['inventory'])
        print(data[item_name_lower]['description']['sac'])
        print(insure_tag)
        print(data[item_name_lower]['description']['limited'])
        print(data[item_name_lower]['description']['spells'])
        print(data[item_name_lower]['description']['value'])
    else:
        print(item_name)
        print()
        print()
        print()
        print(insure_tag)
        print()
        print()

def main():
    item_name = sys.argv[1]
    
    insure_tag = ""
    if "(insured)" in item_name:
        insure_tag = "(insured)"
        
    item_name = item_name.replace("_", "'")
    item_name = item_name.replace("(invisible)", "")
    item_name = item_name.replace("(insured)", "")
    item_name = item_name.replace("(glowing)", "")
    item_name = item_name.replace("(humming)", "")
    item_name = item_name.strip()
    find_item(item_name, insure_tag)


if __name__ == "__main__":
    main()
