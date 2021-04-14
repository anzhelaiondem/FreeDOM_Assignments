import support_functions as sf
import time


# Creates list of stars includes id, ra, declination and mean magnitude elements(in string type).
def extract_id_ra_dec_mag_list(file_path) -> list:
    file_row = []
    elements_of_row = []
    id_ra_dec_mag_list = []
    file = open(f"{file_path}")
    for row in file:
        file_row.append(row)  # Here we have every row as a single string.
    for i in range(1, len(file_row)):
        item = sf.split_str(file_row[i])
        elements_of_row.append(item)
    file.close()
    for row in elements_of_row:
        id_ra_dec_mag_list.append([row[7], row[0], row[1], row[22]])
    return id_ra_dec_mag_list


# Extracts only those Stars the RA and declination of which are within the given FOV.
def filter_extracted_list(ra, dec, fov_h, fov_v, extracted_list) -> list:
    filtered_extracted_list = []
    filtered_extracted_list.append(extracted_list[0])  # Here it adds the titles of columns.
    for radec in extracted_list:
        try:
            if ((float(radec[1]) - float(fov_h) / 2) < (float(ra)) < float(radec[1]) + float(fov_h) / 2
                    and float(radec[2]) - float(fov_v) / 2 < float(dec) < float(radec[2]) + float(fov_v) / 2):
                filtered_extracted_list.append(radec)
        except ValueError:
            pass
    return filtered_extracted_list


# Sorts and takes mentioned N number of Stars
def n_brightest_stars_list(filter_extracted_list, n):
    n_brightest_stars = []
    n_brightest_stars.append(filter_extracted_list[0])  # Here it adds the titles of columns.
    sf.sort_descending(filter_extracted_list)
    try:
        for i in range(1, int(n) + 1):
            n_brightest_stars.append(filter_extracted_list[i])
    except IndexError:
        print("Given number is bigger than the available stars' number.")
    return n_brightest_stars


# Adds "distance" attribute to the extracted and sorted n stars.
def final_n_stars_list(filtered_extracted_list):
    final_n_stars = []
    filtered_extracted_list[0].append("distance")
    final_n_stars.append(filtered_extracted_list[0])
    for i in range(1, len(filtered_extracted_list)):
        final_n_stars.append(sf.distance_calculation(filtered_extracted_list[i]))
    return final_n_stars


def output(final_list):
    ct = time.strftime('%Y-%m-%d %H:%M:%S')
    file = open(f"{ct}.csv", "w")
    for row in final_list:
        file.write(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {(row[4])} \n")
    file.close()
