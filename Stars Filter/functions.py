file_path = "/home/aib/Desktop/Git_Assignment1/Stars Filter/337.all.tsv"


# Sorting functions: ascending and descending.
def sort_ascending(list):
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def sort_descending(list):
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


# String splitter.
def split_str(string):
    split_value = []
    tmp = ''
    for c in string:
        if c == '\t' or c == '\n':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    return split_value


# Creating lists from a file.
def file_to_list():
    f_all = []
    f_list = []
    file = open("/home/aib/Desktop/Git_Assignment1/Stars Filter/337.all.tsv")
    for row in file:
        f_all.append(row)  # Here we have every row as a single string.
    for i in range(2, len(f_all)):  # Here we split every row into list (skipping first 2 lines)
        f_list.append(split_str(f_all[i]))
    return f_list


# List of RA in float type.
def ra_ep2000_list():
    ra_list = []
    f_list = file_to_list()
    for item in range(0, len(f_list)):
        try:
            ra_list.append(float(f_list[item][0]))
        except ValueError:
            pass
    return ra_list


# List of DEC in float type.
def dec_ep2000_list():
    dec_list = [];
    f_list = file_to_list()
    for item in range(0, len(f_list)):
        try:
            dec_list.append(f_list[item][1])
        except ValueError:
            pass
    return dec_list
