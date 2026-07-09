from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import requests
import os

# .env 읽기
load_dotenv()

mcp = FastMCP("Naver News")

CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

print("CLIENT_ID =", CLIENT_ID)
print("CLIENT_SECRET =", CLIENT_SECRET[:5] + "*****" if CLIENT_SECRET else None)

@mcp.tool()
def search_stock_news(company: str, display: int = 5):
    """
    Search latest stock news from Naver OpenAPI.
    """

    url = "https://openapi.naver.com/v1/search/news.json"

    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
    }

    params = {
        "query": company,
        "display": display,
        "sort": "date",
    }

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    items = response.json()["items"]

    result = []

    for item in items:
        result.append(
            {
                "title": item["title"],
                "description": item["description"],
                "link": item["link"],
                "pubDate": item["pubDate"],
            }
        )

    return result


if __name__ == "__main__":
    mcp.run()