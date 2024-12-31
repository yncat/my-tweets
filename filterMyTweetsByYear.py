import json
import pytz
from datetime import datetime

year = 2024
filename = "tweets.json"
timezone = pytz.timezone("Asia/Tokyo")
results = []

with open(filename, "r", encoding="UTF-8") as file:
    tweets = json.load(file)

for tweet in tweets:
  tw = tweet["tweet"]
  # created_at example: Mon Dec 30 04:10:25 +0000 2024
  created_at = datetime.strptime(tw["created_at"], "%a %b %d %H:%M:%S %z %Y").astimezone(timezone)
  if created_at.year == year:
    results.append({"created_at": created_at, "full_text": tw["full_text"]})

results.sort(key=lambda x: x["created_at"])

for result in results:
  print("%s -- %s"% (result["full_text"], result["created_at"]))
