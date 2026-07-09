from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("Naver News")

CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")


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