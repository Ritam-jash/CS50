# # using request modules to acess the itunes database
""" import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json()) """


# acess the itunes using request & using json.dumps & indent=2 for a good looking
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2 ))



# Try another way to acess the all playlist of music
# Final finishing
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# responce = requests.get("https://itunes.apple.com/search?entity=song&limit=10000&term=" + sys.argv[1])
# o = responce.json()

# for result in o["results"]:
#     print(result["trackName"])