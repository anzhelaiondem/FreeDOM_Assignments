def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def sort_ascending(list):
    for i in range(0, length(list)):
        for j in range(0, length(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def sort_descending(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


l = [86, 345, 6, 7, 3, 4, 56, 6, 4, 4, 6,]


