import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=25.05&longitude=121.53&current=temperature_2m,relative_humidity_2m,weather_code"

response = requests.get(url)
data = response.json()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("資料抓取完成，已存成 data.json")