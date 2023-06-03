import numpy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def Practice(game):
  fig = plt.figure(figsize=(20,5))
  heights = 5*[1]
  widths = 4*[1]
  
  G = gridspec.GridSpec(5,4,height_ratios=heights,width_ratios=widths,wspace=0,hspace=0)
  
  plt.subplot(G[2:4,0],facecolor='lightblue')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.5,0.5,'Employer',ha='center',va='center',size=12)

  plt.subplot(G[2,1],facecolor='blue')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.5,0.5,game['Employer'][0],ha='center',va='center',size=12)

  plt.subplot(G[3,1],facecolor='white')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.5,0.5,game['Employer'][1],ha='center',va='center',size=12)
  
  plt.subplot(G[0,2:4],facecolor='white')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.5,0.5,'Employee',ha='center',va='center',size=12)

  plt.subplot(G[1,2],facecolor='white')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.5,0.5,'Employee[0]',ha='center',va='center',size=12)

  plt.subplot(G[1,3],facecolor='white')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.5,0.5,'Employee[1]',ha='center',va='center',size=12)

  plt.subplot(G[4,:],facecolor='white')
  plt.xticks([])
  plt.yticks([])
  plt.text(0.1,0.5,game['How It Works'][0],ha='center',va='center',size=12)

  plt.show()
