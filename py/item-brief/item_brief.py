import json
import sys


def find_item(fname):
    with open("data/items.json") as f:
        data = json.load(f)

    if fname in data:
        print(fname)
        print(data[fname]['description']['equipped'])
        print(data[fname]['description']['inventory'])
    else:
        print(fname)
        print()
        print()


def main():
    fname = sys.argv[1]
    fname = fname.replace("(invisible)", "")
    fname = fname.replace("(insured)", "")
    fname = fname.replace("(glowing)", "")
    fname = fname.replace("(humming)", "")
    fname = fname.strip()

    find_item(fname)


if __name__ == "__main__":
    main()
