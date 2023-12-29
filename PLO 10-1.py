import requests
import json
import numpy
import pandas
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
url = '{}{}'.format(fixed,'namq_10_lp_ulc')
metadata = requests.get(url).json()
data = pandas.Series(metadata['value']).rename(index=int).sort_index()
n = 1 # Initialize the result to 1
for num in metadata['size']:
  n *= num
data = data.reindex(range(0,n),fill_value=0)
structure = [pandas.DataFrame({key:val for key,val in metadata['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in metadata['id']]
data.index = pandas.MultiIndex.from_product(structure,names=metadata['id'])
mydata = data.reset_index()

mydata = mydata[mydata.geo=='Spain']
mydata = mydata[mydata.unit=='Index, 2015=100']
mydata = mydata[mydata['s_adj'].str.contains('Unadjusted')]
mydata = mydata[mydata['na_item'].str.contains('work')]
mydata = mydata[mydata.time.str.contains('20')]
mydata = mydata.pivot(index='time',columns='na_item',values=0).reset_index()

plt.figure(figsize=(20,10))  # Adjust the figure size if needed
plt.plot(mydata.time,mydata['Nominal unit labour cost based on hours worked'], label='Nominal unit labor cost based on hours worked',marker='o',color='blue')  # Plotting variable 1
plt.plot(mydata.time,mydata['Real labour productivity per hour worked'], label='Real labor productivity per hour worked',marker='x',color='red')  # Plotting variable 2
ticks = numpy.arange(1,len(mydata.time)+1)
labels = ['' if i % 4 != 0 else 'Q'+str(i) for i in ticks]
plt.xticks(ticks,labels,fontsize=12)
plt.xlabel('Quarters from 2000 to 2023')
txt = [int(num) if (i + 1) % 4 == 0 else '' for i,num in enumerate(mydata['Nominal unit labour cost based on hours worked'])]
for i in numpy.arange(0,len(txt)):
  plt.annotate(txt[i],(ticks[i],mydata['Nominal unit labour cost based on hours worked'][i]),textcoords="offset points",xytext=(0,10),ha='center',color='blue')
txt = [int(num) if (i + 1) % 4 == 0 else '' for i,num in enumerate(mydata['Real labour productivity per hour worked'])]
for i in numpy.arange(0,len(txt)):
  plt.annotate(txt[i],(ticks[i],mydata['Real labour productivity per hour worked'][i]),textcoords="offset points",xytext=(0,10),ha='center',color='red')
ticks = numpy.arange(75,130)
labels = ['' if i % 5 != 0 else str(i) for i in ticks]
plt.yticks(ticks,labels,fontsize=12)


plt.ylabel('Index (2015=100)')
plt.legend(loc='upper left',fontsize=14)
plt.grid(True)
plt.box(False)
plt.show()
