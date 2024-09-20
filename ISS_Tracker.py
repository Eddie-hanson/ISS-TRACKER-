import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder


url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open('ISS.txt', 'w')
file.write('There are currently ' +
           str(result['number']) + ' astronauts on the ISS:\n\n')
people = result['people']

for p in people:
    file.write(p['name'] + 'is on boad the ISS\n\n')

g = geocoder.ip('me')
file.write('Your current lat/long is:' + str(g.latlng))
file.close()
webbrowser.open('ISS.txt')

screen = turtle.Screen()
screen.setup(1500, 760)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('Worldmap.gif')
screen.register_shape('ISS.gif')

iss = turtle.Turtle()
iss.shape('ISS.gif')
iss.setheading(45)
iss.penup()

while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    print('\n Latitude: ', lat, ' - ', 'Longitude: ', lon)

    iss.goto(lon, lat)
    time.sleep(5)
