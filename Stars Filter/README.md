# Stars Filter
## Summary
This program is designed to search in the given .tsv data file and create a .csv file that will contain the N brightest stars that are within the defined frames of equatorial coordinates. The frame is based on the provided horizontal and vertical field of view (fov\_h, fov\_v), right ascension (ra), and declination (dec). The file also contains stars' id, equatorial coordinates (ra, dec), brightness (magnitude) and the distance from the earth (very rough calculation). The data is sorted in ascending order based on distance.

### Input
1 The absolute path of the file/data (the file should be in .tsv format).
2 Right ascension.
3 Declination.
4 Field of view: vertical
5 Field of view: horizontal
6 The number of stars to see in the output file.

### Output
CVS file with the name of current date and time. 
The location of the output file is the same folder where the program files are. 
The file contains five attributes of the N files: id of a star (source\_id), right ascension (ra\_ep2000), declination (dec\_ep2000), mean magnitude (phot\_g\_mean\_mag), and distance (distance).

## Description of the program structure
The program consists of three modules: main.py, main-functions.py, and support_functions.py.
#### main.py
This module contains the main running function. 
##### Running the program
After running the program, it asks for the following inputs:\
_Please indicate a database file path:\
_Right Ascension:\
_Declination:\
_Field of View - vertical:\
_Field of View - horizontal:\
_Number of stars to see in the output file:\
After providing right path and numbers, the program starts to run all five functions of the main\_functions.py module.
#### main\_functions.py
This module contains the following 5 functions:
##### def extract_id\_ra_dec\_mag\_list(file\_path) -> list:
This function takes the provided path of the data, splits it into a list of stars’ attributes, extracts only needed attributes/columns (id, ra, dec, mag) and as an output gives a list of stars that contain only extracted 4 attributes.
##### def filter\_extracted\_list(ra, dec, fov\_h, fov\_v, extracted\_list) -> list:
This function checks if the star's coordinates are within the field of view frame (taking the provided ra dec as a center of the frame). 
##### def n\_brightest\_stars\_list(filter\_extracted\_list, n):
Taking the filtered and extracted list of stars (which was done in the previous two functions), sorts it by the brightness (based on the mean magnitude) of the star, and then provides a list of the top N stars as an output.
##### def final\_n\_stars\_list(filtered\_extracted\_list):
This function takes sorted N stars from the previous function, adds the “distance” attribute (taking it from the support\_functions.py module) and provides the final list of the N stars. As the distance calculation is based on the mean magnitude (see formula below), therefore it doesn’t need to be sorted again.
##### def output(final\_list):
By taking the final list of the stars, this function creates a .csv extension file, writes all N stars into the file with “,” separation and put the file into the same “Stars Filter” folder. The name of the file is the current date and time.
#### support\_functions.py
This module consists of the following three functions that support the main\_functions.py module:
##### def split\_str(s, sep='\t'):
The function is used in the “def extract\_id\_ra\_dec\_mag\_list(file\_path) -> list:” function for splitting the data file into list of the stars.

##### def sort\_descending(f\_list):
Bubble sort, with descending nature, is used in the "def final\_n\_stars\_list(filtered\_extracted\_list)" function to sort the stars with their brightness.
##### def distance_calculation(row\_from\_sorted\_n\_stars):
The calculation of distance is based on the following formula m−M=5×log(D)−5, where m is the apparent magnitude, M is the absolute magnitude and D is the distance. With a very rough approach, the average magnitude was taken for (m-M).
#### Limitations of the program
_Provided .tsv file\
The file should have exact form regarding the attributes/columns and their index:\
right ascension index: 0\
declination index: 1\
id index: 7\
mean magnitude index: 22\
_Inputted data:\
Inputted right ascension should be in degrees.\
All inputs (except the file path) should be numbers.\
_If N is greater than the final list, the program gives a warning message, no output file.
