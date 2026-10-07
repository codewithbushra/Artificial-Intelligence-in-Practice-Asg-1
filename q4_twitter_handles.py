"""
Question 4 - Find all unique Twitter handles (@name) in the tweets.
Run:  python q4_twitter_handles.py
Make sure 'Twitter US Airline Sentiment.csv' is in the same folder.
"""
import re
import pandas as pd

tweets = pd.read_csv('Twitter US Airline Sentiment.csv')['text'].dropna()

handles = set()                                  # set -> no duplicates
for tweet in tweets:
    handles.update(re.findall(r'@[A-Za-z0-9_]+', tweet))

print("=" * 60)
print("QUESTION 4 - Unique Twitter Handles")
print("=" * 60)
print(f"Total unique handles found: {len(handles)}")
print()
print("All handles (sorted):")
for i, h in enumerate(sorted(handles), 1):
    print(f"{i:>4}. {h}")
