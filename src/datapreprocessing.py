import json
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text: str) -> str:
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove Twitter mentions and hashtags
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert text to lowercase
    text = text.lower()
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

# Load raw tweet data from stock_tweets.json (structured as a dictionary)
with open("stock_tweets.json", "r") as infile:
    raw_data = json.load(infile)

processed_data = {}

# Iterate over each stock symbol and its tweets
for stock, tweets in raw_data.items():
    processed_tweets = []
    for tweet in tweets:
        # If tweet is a dict with key "text", extract it; otherwise, assume tweet is a string.
        tweet_text = tweet["text"] if isinstance(tweet, dict) and "text" in tweet else tweet
        cleaned = clean_text(tweet_text)
        processed_tweets.append({
            "original_text": tweet_text,
            "cleaned_text": cleaned
        })
    processed_data[stock] = processed_tweets

# Save the processed data to a new JSON file
with open("cleaned_tweets.json", "w") as outfile:
    json.dump(processed_data, outfile, indent=4)

print("Preprocessing complete. Processed data saved to cleaned_tweets.json.")
