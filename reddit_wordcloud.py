from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


d = path.dirname(__file__)

# read the text
text = open(path.join(d, 'redditdata.txt')).read()

wordcloud = WordCloud().generate(text)

# display the image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
