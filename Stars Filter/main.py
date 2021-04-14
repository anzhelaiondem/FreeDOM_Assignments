import main_functions as mf


def main():
    file_path = input("Please indicate a database file path: ")
    ra = input("Right Ascension: ")
    dec = input("Declination: ")
    fov_v = input("Field of View - vertical: ")
    fov_h = input("Field of View - horizontal: ")
    n = input("Number of stars to see in the output file: ")
    stars_id_ra_dec_mag_list = mf.extract_id_ra_dec_mag_list(file_path)
    filtered_id_ra_dec_mag_list = mf.filter_extracted_list(ra, dec, fov_h, fov_v, stars_id_ra_dec_mag_list)
    n_brightest_stars_list = mf.n_brightest_stars_list(filtered_id_ra_dec_mag_list, n)
    final_n_stars_id_ra_dec_mag_dist_list = mf.final_n_stars_list(n_brightest_stars_list)
    mf.output(final_n_stars_id_ra_dec_mag_dist_list)


if __name__ == "__main__":
    main()
