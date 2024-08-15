# My Home Routes
Interogates routes and saves results using the Google Maps API

## Requirements
* Python 3 (get it from https://www.python.org/)
* `pip install -U googlemaps`
* `python -m pip install -U matplotlib`
* `pip install numpy`
* Each Google Maps Web Service request requires an API key or client ID. API keys are generated in the 'Credentials' page of the 'APIs & Services' tab of [Google Cloud console](https://console.cloud.google.com/apis/credentials).
* Any text editor for creating/reading a CSV file (i.e. notepad)


## Input
Input is given from the `in` folder. The folder will be located at the same level as the `main.py` script. Before running the program, there are multiple files that require an update:
* `key.key` - copy the generated key for `API Key for Google Maps Web Service` in the `key.key` file
* `to.csv` - enter the start address, one per line, as they would appear in the [Google Maps](https://www.google.com/maps) search input
* `from.csv` - enter the end address, one per line, as they would appear in the [Google Maps](https://www.google.com/maps) search input
* `routes.csv` - enter tuples of start and end addresses, one per line, which will be represented in the generated graph

**_NOTE:_** If one address contains comma characters, then place the address between quotation marks, i.e. *"Piața Victoriei, București"*


## How To Run 

After updating the input files, one can run the program in two modes, either for gathering real time traffic information at preset time intervals and another mode that uses the results from gathering the traffic data and plots the time necessary to drive between addreses defined in the `routes.csv` file

### Gather traffic information at default 1h time intervals

`python .\main.py -g` - a results csv file will be created for the current day of the month

### Gather traffic information at custom time intervals

`python .\main.py -g -i 7200` - gathers results for the current day of the month at 2h time intervals

### Plot graph 

`python .\main.py -p ".\in\routes.csv" -r ".\results\results_08_11_2024.csv` - opens a single graph that displays the necessary driving time between the defined routes, using the gathered data from teh results file

## Output
If the file `result_<month>_<day>_<year>.csv` exists, then the results will be appended to it, otherwise the file will be created.

One output line will contain the following fields in the given order:
* Start Address
* End Address
* Hour
* Distance
* Duration

## Google Maps API
More details can be found at [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python?tab=readme-ov-file).