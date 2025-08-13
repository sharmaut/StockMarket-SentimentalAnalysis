from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from twitter_stream import scrape_tweets
from news_scrape import scrape_news
from tweets_analysis import analyze_tweet_sentiment
from news_analysis import analyze_news_sentiment

app = FastAPI()

class StockRequest(BaseModel):
    symbol: str

@app.post("/analyze")
def analyze_stock(request: StockRequest):
    symbol = request.symbol.upper().strip()
    print(f"Received request for: {symbol}")

    # Dynamically scrape tweets and news
    tweets_data = scrape_tweets(symbol, max_tweets=10)
    news_data = scrape_news(symbol)
    
    # Check if data is returned
    if not tweets_data.get(symbol):
        raise HTTPException(status_code=404, detail="No tweet data found for this symbol.")
    if not news_data.get(symbol):
        raise HTTPException(status_code=404, detail="No news data found for this symbol.")
    
    # Run sentiment analysis on the scraped data
    tweet_sentiments = analyze_tweet_sentiment(tweets_data[symbol])
    news_sentiments = analyze_news_sentiment(news_data[symbol])
    
    # Log counts for debugging
    print(f"Scraped {len(tweets_data[symbol])} tweets and {len(news_data[symbol])} news articles for {symbol}.")

    # Return the combined sentiment results
    return {
        "symbol": symbol,
        "tweets_sentiment": tweet_sentiments,
        "news_sentiment": news_sentiments
    }
