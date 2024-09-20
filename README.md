# ISS Tracker Application

This project is an ISS (International Space Station) tracking application that shows the current location of the ISS in real-time using a NASA API. The application also displays a list of astronauts currently onboard the ISS, retrieves the user's geographical coordinates, and provides a graphical view of the ISS's movement on a world map.

## Features

- Tracks the current location of the ISS using real-time data.
- Displays the list of astronauts currently aboard the ISS.
- Retrieves and displays the user's current latitude and longitude.
- Uses Turtle graphics to visualize the ISS's position on a world map.
- Logs the ISS data and user location into a text file (`ISS.txt`).
- Automatically opens the text file after logging.

## Requirements

Make sure you have the following dependencies installed:

- `Python 3.6+`
- `turtle` (built-in Python module)
- `urllib`
- `json`
- `geocoder`
- `time`
- `webbrowser`

Install external libraries by running:
pip install geocoder

## Setup

Clone or download the project to your local machine.
create a virtual environment python -m venv
Install the required Python packages.
Run the script using Python.
python iss_tracker.py

## How It Works

The app uses the Open Notify API to retrieve real-time data about the ISS's position and astronauts aboard.
The Turtle graphics library is used to visualize the ISS's location on a world map, and the data is updated every 5 seconds.
Your current geographical location is fetched using the geocoder library.

### Output

The list of astronauts aboard the ISS is saved to a text file (ISS.txt) and automatically opened in the default text editor.
The Turtle graphics window displays the ISS moving across a world map in real-time based on data fetched from the NASA API.

### External Libraries Used

geocoder for retrieving the user's current location.
turtle for drawing and displaying the ISS on the map.
