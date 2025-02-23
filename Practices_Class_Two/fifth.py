# command line arguments
import sys

print("My name is", sys.argv[1])




# now solve the error
import sys

try:
    print("My name is", sys.argv[1])
except IndexError:
    print("Few arguments")




# Now we put the value then we can handel the error
import sys

if len(sys.argv) < 2:
    print("Too few argumrnt")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("My name is", sys.argv[1])




# Now we put infinite value on sys.argv
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
for sys in sys.argv[1: ]:
    print("My name is," , sys)





# API
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())




# Best way to fomating the data
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json(), indent=2))




# Now we try to get value
import requests
import json
import sys

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1])

o = response.json()

for result in o["results"]:
    print(result["trackName"], result["artistName"], sep=", ")

# https://itunes.apple.com/search?entity=song&limit=1&term=Weezer
# https://itunes.apple.com/search?entity=song&limit=1&term=Weezer
# https://itunes.apple.com/search?entity=song&limit=1&term=Weezer
# https://itunes.apple.com/search?entity=song&limit=1&term=Weezer
# https://itunes.apple.com/search?entity=song&limit=1&term=Weezer
# https://itunes.apple.com/search?entity=song&limit=1&term=Weezer

