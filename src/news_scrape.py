from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def scrape_news(stock_symbol: str) -> dict:
    url = f"https://finance.yahoo.com/quote/{stock_symbol}/news?p={stock_symbol}"
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=500)  # slow motion for debugging
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        
        try:
            page.goto(url, timeout=30000)
            page.wait_for_load_state("domcontentloaded", timeout=30000)
        except Exception as e:
            print(f"Error navigating to {url}: {e}")
            browser.close()
            return {stock_symbol: []}
        
        # Wait additional time for JS to load dynamic content
        time.sleep(15)
        
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        # Debug: print the HTML snippet
        html_snippet = soup.prettify()[:2000]
        print("HTML snippet:", html_snippet)
        
        articles = []
        for item in soup.find_all("h3", class_="clamp  yf-82qtw3"):
            headline = item.get_text(strip=True)
            link_tag = item.find_parent("a")
            link = "https://finance.yahoo.com" + link_tag.get("href", "") if link_tag else ""
            articles.append({
                "stock": stock_symbol,
                "headline": headline,
                "link": link
            })
        
        print(f"Found {len(articles)} articles for {stock_symbol}")
        browser.close()
        return {stock_symbol: articles}

if __name__ == "__main__":
    print(scrape_news("AAPL"))
