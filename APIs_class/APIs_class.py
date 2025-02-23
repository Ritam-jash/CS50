# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))


## Chatgpt solution
# import json
# import requests
# import sys
# import urllib.parse

# if len(sys.argv) != 2:
#     print("Usage: script.py <search-term>")
#     sys.exit(1)

# # URL encode the search term
# search_term = urllib.parse.quote(sys.argv[1])

# try:
#     response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={search_term}")
#     response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
#     data = response.json()
#     print(json.dumps(data, indent=2))
# except requests.exceptions.RequestException as e:
#     print(f"Error: {e}")
#     sys.exit(1)

# Track the itunes all playlist using json & requests
# Final solution
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

responce = requests.get("https://itunes.apple.com/search?entity=song&limit=9999&term=" + sys.argv[1])

o = responce.json()
for result in o["results"]:
    print(result["trackName"])