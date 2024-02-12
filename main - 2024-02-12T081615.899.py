import subprocess

# Install TextBlob library using pip
subprocess.run(['pip', 'install', 'textblob'])

from textblob import TextBlob

# Sample conversation
conversation = [
    "Excited for the Super Bowl this weekend!",
    "I hope my team wins!",
    "Feeling nervous about the game.",
    "The halftime show was amazing!",
    "Disappointed with the outcome of the game."
]

# Analyze sentiment of each message
sentiments = []
for message in conversation:
    blob = TextBlob(message)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    sentiments.append((message, sentiment))

# Print sentiment of each message
for message, sentiment in sentiments:
    print(f"Message: {message} - Sentiment: {sentiment}")

