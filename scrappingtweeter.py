import snscrape.modules.twitter as sntwitter
import pandas as pd

query = input("what words you want to find in twitter?")
num_tweets = int(input(" Total tweets want to find?"))
tweets = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= num_tweets:
        break
    tweets.append((tweet.date, tweet.rawContent, tweet.user.username, tweet.likeCount))

tweet_df = pd.DataFrame(tweets, columns = ['Date', 'Content', 'Username', 'Like Count']) 
print(tweet_df)

tweet_df.to_csv('tweetscraping.csv', index=False)