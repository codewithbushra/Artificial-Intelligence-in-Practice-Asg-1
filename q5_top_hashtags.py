"""
Question 5 - Top 10 most frequent hashtags in the tweets.
Run:  python q5_top_hashtags.py
The chart is SAVED as a PNG and also shown on screen.
"""
import re
from collections import Counter
import pandas as pd

tweets = pd.read_csv('Twitter US Airline Sentiment.csv')['text'].dropna()

counter = Counter()
for tweet in tweets:
    counter.update(re.findall(r'#(\w+)', tweet))   # capture the word after '#'

top10 = counter.most_common(10)

print("=" * 60)
print("QUESTION 5 - Top 10 Most Frequent Hashtags")
print("=" * 60)
for rank, (tag, count) in enumerate(top10, 1):
    print(f"{rank:>2}. #{tag:<25} {count} times")

# Bar chart of the top 10
import matplotlib.pyplot as plt
labels = [f'#{t}' for t, _ in top10][::-1]
counts = [c for _, c in top10][::-1]
plt.figure(figsize=(8, 4.5))
plt.barh(labels, counts, color='#C44E52')
plt.title('Top 10 Most Frequent Hashtags')
plt.xlabel('Frequency')
plt.tight_layout()

plt.savefig('top10_hashtags.png', dpi=150)   # SAVE the figure
print("Figure saved: top10_hashtags.png")

plt.show()