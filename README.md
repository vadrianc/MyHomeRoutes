# My Home Routes
Interrogates routes and saves results using the Google Maps API.

## How to setup under Windows
* Python 3 (get it from https://www.python.org/)
* `pip install -U googlemaps`
* `python -m pip install -U matplotlib`
* `pip install numpy`
* Each Google Maps Web Service request requires an API key or client ID. API keys are generated in the 'Credentials' page of the 'APIs & Services' tab of [Google Cloud console](https://console.cloud.google.com/apis/credentials).
* Any text editor for creating/reading a CSV file (i.e. notepad)

## How to setup under Raspbian GNU/Linux 12 (bookworm)
Need to create a virtual environment, where we prepare the setup for running the program.

* `python3 -m venv /path/to/environment`
* `source /my_home_routes/bin/activate`
* `/path/to/environment/bin/pip install -U googlemaps`
* `/path/to/environment/bin/python3 -m pip install -U matplotlib`
* `/path/to/environment/bin/pip install numpy`

Replace `/path/to/environment` with the path of your choosing. Some of the above commands may require elevated privileges, so use `sudo` in front of them.

### Known issues
1. Failure to import `numpy` caused by *ImportError: libopenblas.so.0: cannot open shared object file: No such file or directory* - install the missing dependency by running `sudo apt-get install libopenblas-dev`.
2. Failure to import `plotter` caused by *ImportError: libopenjp2.so.7: cannot open shared object file: No such file or directory* - install missing dependency by running `sudo apt-get install libopenjp2-7`

## Input
Input is given from the `in` folder. The folder will be located at the same level as the `main.py` script. Before running the program, there are multiple files that require an update:
* `key.key` - copy the generated key for `API Key for Google Maps Web Service` in the `key.key` file
* `to.csv` - enter the start address, one per line, as they would appear in the [Google Maps](https://www.google.com/maps) search input
* `from.csv` - enter the end address, one per line, as they would appear in the [Google Maps](https://www.google.com/maps) search input
* `routes.csv` - enter tuples of start and end addresses, one per line, which will be represented in the generated graph

**_NOTE:_** If one address contains comma characters, then place the address between quotation marks, i.e. *"Piața Victoriei, București"*.


## How To Run 

After updating the input files, one can run the program in two modes, either for gathering real time traffic information at preset time intervals and another mode that uses the results from gathering the traffic data and plots the time necessary to drive between addresses defined in the `routes.csv` file

**_NOTE:_** Examples below are for Windows environments. For other environments, i.e. Linux, adjust the syntax accordingly.

### Gather traffic information at default 1h time intervals

`python .\main.py -g` - a results csv file will be created for the current day of the month.

### Gather traffic information at custom time intervals

`python .\main.py -g -i 7200` - gathers results for the current day of the month at 2h time intervals.

### Plot graph 

`python .\main.py -p ".\in\routes.csv" -r ".\results\results_08_11_2024.csv"` - opens a single graph that displays the necessary driving time between the defined routes, using the gathered data from teh results file.

### Running under Linux by detaching from the current ssh session

`sudo nohup /my_home_routes/bin/python3 main.py -g & >/dev/null 2>&1`

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