# where-was-i
Simple Script to Parse Google Maps History

##
Simple script to quickly calculate the number of days in a year you have visited a type of place such as work. 

## prerequisites
Google Maps data downloaded https://www.howtogeek.com/725241/how-to-download-your-google-maps-data/

## usage
```sh
usage: where_was_i.py [-h] [--semantic_type SEMANTIC_TYPE] year_folder

Count visits to a specific location in a given year from Google Maps history.

positional arguments:
  year_folder           Path to the folder containing the location history JSON files for the specified year

options:
  -h, --help            show this help message and exit
  --semantic_type SEMANTIC_TYPE
                        Semantic type of the location (e.g., TYPE_WORK, TYPE_HOME)
```
### uxample to get the number of in the year 2023 at work
`python where_was_i.py ./timeline-location-history/2023/`
