# Filtering-Stars
## Summary
This program is designed to create a .csv file that will contain the N brightest stars in the specified frame. The frame is based on the provided horizontal and vertical field of view (fov-h, fov-v), right ascension (ra), and declination (dec). The file also contains an identifier, equatorial coordinates (ra, dec), brightness (magnitude) and distance to stars. The data is sorted in ascending order based on distance.

### Input
1 The absolute path of the file/data (the file should be in .tsv format).
2 Right ascension.
3 Declination.
4 Field of view: vertical
5 Field of view: horizontal
6 The number of stars to see in the output file.

### Output
CVS file with the name of current date and time. 
The location of the output file is the same folder where the program is. 
The file contains five attributes of the N files: id, ra, dec, mean magnitude, and distance. 



