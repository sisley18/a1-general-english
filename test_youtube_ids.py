import urllib.request
import json

candidate_ids = [
    "n56r-jL2R8Q", # Lesson 1
    "aPzY5_9zO2A", # Lesson 2
    "aPzY5-9zO2A",
    "F3a7N7P6_g0",
    "G2sT23a07t8",
    "9M7OqfE8WwY",
    "xOcmG4H3K20",
    "6uU5oB0w9aQ",
    "4qD7oA9q8wM",
    "2pY2a2h8x3M",
    "8y12Q9b9c9Q",
    "s63XgM-a4Uo",
    "H2aHn0o_2s8",
    "_F2PZcslXlA"
]

valid_ids = []
for vid in candidate_ids:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"VALID: {vid} - {data['title']}")
            valid_ids.append((vid, data['title']))
    except Exception as e:
        print(f"INVALID: {vid} - {e}")

print("Valid IDs found:")
print(valid_ids)
