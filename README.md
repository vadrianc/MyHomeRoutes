# My Home Routes
Interogates routes and saves results using the Google Maps API

## Requirements
* Python 3 (get it from https://www.python.org/)
* `pip install -U googlemaps`
* Each Google Maps Web Service request requires an API key or client ID. API keys are generated in the 'Credentials' page of the 'APIs & Services' tab of [Google Cloud console](https://console.cloud.google.com/apis/credentials).
* Any text editor for creating/reading a CSV file (i.e. notepad)
* `python -m pip install -U matplotlib`
* `pip install numpy`

## Input
Input is given from the `in` folder, from the `tracks.csv` file. The folder will be located at the same level as the `main.py` script. Two files need to be created under the `in` folder:
* key.key
* tracks.csv

### API Key for Google Maps Web Service request
Copy the generated key in the `key.key` file

### Tracks
The `tracks.csv` file will contain two values per row, separated by a `,` character.
The first field represents the start address and the second field the end address.
If one address contains comma characters, then place the address between quotation marks, i.e. *"Piața Victoriei, București"*

## How To Run 
In the terminal, navigate to where the `main.py` file is located
Run the script by typing: `python main.py` and press `Enter`

## Output
If the file `result_<month>_<day>_<year>.csv` exists, then the results will be appended to it, otherwise the file will be created near the `main.py` script.

One output line will contain the following fields in the given order:
* Start Address
* End Address
* Hour
* Distance
* Duration

## Google Maps API
More details can be found at [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python?tab=readme-ov-file).