# tweet_sentiment.py
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

nltk.download('vader_lexicon')

def analyze_tweet_sentiment(tweets: list) -> list:
    """
    Given a list of tweet dictionaries with a "text" key,
    compute sentiment scores using VADER and TextBlob.
    """
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for tweet in tweets:
        text = tweet["text"]
        vader_scores = analyzer.polarity_scores(text)
        tb_sentiment = TextBlob(text).sentiment
        results.append({
            "text": text,
            "vader": vader_scores,
            "textblob": {
                "polarity": tb_sentiment.polarity,
                "subjectivity": tb_sentiment.subjectivity
            }
        })
        
    return results
