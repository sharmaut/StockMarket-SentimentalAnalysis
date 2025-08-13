# tweet_scraper.py
import json
import time
from playwright.sync_api import sync_playwright

def scrape_tweets(stock_symbol: str, max_tweets: int = 20) -> dict:
    tweets = set()
    tweet_data = []

    with sync_playwright() as pw:
        # Load the saved session state
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state="twitter_state.json",  # Reuse the session
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()

        search_url = f"https://twitter.com/search?q={stock_symbol}&f=live"
        page.goto(search_url)
        time.sleep(5)

        try:
            page.wait_for_selector("[data-testid='tweet']", timeout=30000)
        except Exception as e:
            print(f"Error: Tweet selector not found for {stock_symbol}.", e)
            browser.close()
            return {stock_symbol: []}

        while len(tweets) < max_tweets:
            tweet_elements = page.query_selector_all("[data-testid='tweet']")
            for tweet in tweet_elements:
                try:
                    text_element = tweet.query_selector("div[lang]")
                    text = text_element.inner_text() if text_element else tweet.inner_text()
                    if text not in tweets:
                        tweets.add(text)
                        tweet_data.append({"text": text})
                        if len(tweets) >= max_tweets:
                            break
                except Exception as ex:
                    print("Error extracting tweet text:", ex)
                    continue
            page.evaluate("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)

        browser.close()
    return {stock_symbol: tweet_data}
