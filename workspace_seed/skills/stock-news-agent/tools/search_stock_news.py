from langchain_core.tools import tool

@tool
def search_stock_news(company: str):

    """
    Search latest stock news
    """

    return {
        "company": company,
        "articles":[
            {
                "title":"삼성전자 AI 투자 확대",
                "url":"https://..."
            }
        ]
    }