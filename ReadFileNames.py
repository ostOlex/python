import collections


def main():
    lines = []
    list_without_separator = []
    with open('nameslist.txt', 'r') as open_file:
        lines = open_file.readlines()
        for line in lines:
            line_without_sep = line.replace('\n', '')
            list_without_separator.append(line_without_sep)
    print collections.Counter(list_without_separator)

main()
