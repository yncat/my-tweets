import json

filename = "tweets.js"
# remove window.YTD.tweets.part0 = from the first line
with open(filename, "r", encoding="UTF-8") as f:
    lines = f.readlines()
    lines[0] = lines[0].replace("window.YTD.tweets.part0 = ", "")

json_object = json.loads("".join(lines))
# pretty format and save
with open("tweets.json", "w", encoding="UTF-8") as f:
    f.write(json.dumps(json_object, indent=2))
