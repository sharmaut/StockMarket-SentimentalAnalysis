# news_sentiment.py
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

nltk.download('vader_lexicon')

def analyze_news_sentiment(articles: list) -> list:
    """
    Given a list of news article dictionaries (with "headline" key),
    compute sentiment scores using VADER and TextBlob.
    """
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for article in articles:
        headline = article["headline"]
        vader_scores = analyzer.polarity_scores(headline)
        tb_sentiment = TextBlob(headline).sentiment
        results.append({
            "headline": headline,
            "link": article.get("link", ""),
            "vader": vader_scores,
            "textblob": {
                "polarity": tb_sentiment.polarity,
                "subjectivity": tb_sentiment.subjectivity
            }
        })
    return results
