from textblob import TextBlob
file=open('mytxt.txt','r')
txt=file.read()
print(txt)
blob=TextBlob(txt)
sentiment=blob.sentiment.polarity
print(sentiment)
