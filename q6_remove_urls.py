"""
Question 6 - Remove all URLs (http/https) from tweets; return list of them.
Run:  python q6_remove_urls.py
"""
import re
import pandas as pd

tweets = pd.read_csv('Twitter US Airline Sentiment.csv')['text'].dropna()

url_pattern = re.compile(r'https?://[^\s]+')     # http(s):// then everything up to a space

removed_urls = []
cleaned_tweets = []

for tweet in tweets:
    found = url_pattern.findall(tweet)            # URLs in this tweet
    removed_urls.extend(found)                    # collect into one list
    cleaned_tweets.append(url_pattern.sub('', tweet).strip())   # remove from text

print("=" * 60)
print("QUESTION 6 - URLs Removed from Tweets")
print("=" * 60)
print(f"Total URLs removed: {len(removed_urls)}")
print()
print("First 10 removed URLs:")
for u in removed_urls[:10]:
    print("  ", u)
print()
print("First 5 cleaned tweets (no URLs):")
for t in cleaned_tweets[:5]:
    print("  ", t)
