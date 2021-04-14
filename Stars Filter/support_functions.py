def split_str(s, sep='\t'):
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = split_str(s[pos + 1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]


def sort_descending(f_list):
    for i in range(0, len(f_list)):
        for j in range(1, len(f_list) - 1):
            try:
                if float(f_list[j][3]) > float(f_list[j + 1][3]):
                    f_list[j], f_list[j + 1] = f_list[j + 1], f_list[j]
            except ValueError:
                pass
    return f_list


# Function gets a star/row, calculates distance based on the mean magnitude, and appends the list with distance value.
def distance_calculation(row_from_sorted_n_stars):
    try:
        mag = float(row_from_sorted_n_stars[3])
        dist = 10 ** ((mag + 5) / 5)
        row_from_sorted_n_stars.append(str(dist))
    except ValueError:
        pass
    return row_from_sorted_n_stars
