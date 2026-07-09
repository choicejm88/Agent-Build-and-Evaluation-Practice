import os
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv(Path(".env"))

headers = {
    "X-Naver-Client-Id": os.getenv("NAVER_CLIENT_ID"),
    "X-Naver-Client-Secret": os.getenv("NAVER_CLIENT_SECRET"),
}

url = "https://openapi.naver.com/v1/search/news.json"

params = {
    "query": "삼성전자",
    "display": 3,
    "sort": "date"
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.text)