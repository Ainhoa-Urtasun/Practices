import matplotlib.pyplot as plt
from wordcloud import WordCloud
def wordcloud(mydict):
  wc = WordCloud(background_color='white').generate_from_frequencies(frequencies=mydict)
  fig = plt.figure(figsize=(10,5))
  plt.axis("off")
  plt.imshow(wc,interpolation="bilinear")
  return plt.show()

