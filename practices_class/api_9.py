# Acess the itunes api
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())


# TAW with clear json formate
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

responce = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(responce.json(), indent=2))


# print the 50 trackName & artistName
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

responce = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = responce.json()

for result in o["results"]:
    print(result["trackName"], result["artistName"], sep=", ")