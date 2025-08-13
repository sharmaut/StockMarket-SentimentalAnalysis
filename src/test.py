import requests
from bs4 import BeautifulSoup

def scrape_news_fixed() -> dict:
    stock_list = ["AAPL", "TSLA", "MSFT"]  # Fixed list that worked previously
    news_results = {}
    
    for stock in stock_list:
        url = f"https://finance.yahoo.com/quote/{stock}/news?p={stock}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching news for {stock}: {response.status_code}")
            news_results[stock] = []
            continue
        
        soup = BeautifulSoup(response.content, "html.parser")
        articles = []
        
        # Using the selector from when it worked:
        for item in soup.find_all("h3", class_="clamp  yf-82qtw3"):
            headline = item.get_text(strip=True)
            link_tag = item.find_parent("a")
            link = "https://finance.yahoo.com" + link_tag.get("href", "") if link_tag else ""
            articles.append({
                "stock": stock,
                "headline": headline,
                "link": link
            })
        
        news_results[stock] = articles
        print(f"Found {len(articles)} articles for {stock}")
        
    return news_results

if __name__ == "__main__":
    results = scrape_news_fixed()
    print(results)
