from textblob import TextBlob
from newspaper import Article

url='https://timesofindia.indiatimes.com/blogs/kembai-speaks/better-shape-of-the-economy-in-2024/'
article=Article(url)
article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

blob=TextBlob(text)
sentiment=blob.sentiment.polarity #from -1 to 1
print(sentiment)
