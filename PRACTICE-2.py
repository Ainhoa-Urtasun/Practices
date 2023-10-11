import requests
import json
import pandas
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pyproj
import warnings
warnings.filterwarnings("ignore")

fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
url = '{}{}'.format(fixed,'migr_resfas')
metadata = requests.get(url).json()
#print(metadata['label'])
data = pandas.Series(metadata['value']).rename(index=int).sort_index()
n = 1 # Initialize the result to 1
for num in metadata['size']:
  n *= num
data = data.reindex(range(0,n),fill_value=0)
structure = [pandas.DataFrame({key:val for key,val in metadata['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in metadata['id']]
data.index = pandas.MultiIndex.from_product(structure,names=metadata['id'])
mydata0 = data.reset_index()
print(mydata0)
mydata0 = mydata0[mydata0.citizen=='Total']
mydata0 = mydata0[mydata0.reason=='Employment reasons']
mydata0 = mydata0[mydata0.time=='2022']
mydata0 = mydata0[mydata0.sex=='Total']
mydata0 = mydata0[mydata0.age=='Total']
mydata0 = mydata0[['geo',0]]
mydata0.rename(columns={0:'Migrants'},inplace=True)
mydata0.rename(columns={'geo':'ADMIN'},inplace=True)

fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
url = '{}{}'.format(fixed,'lfsi_emp_a')
metadata = requests.get(url).json()
#print(metadata['label'])
data = pandas.Series(metadata['value']).rename(index=int).sort_index()
n = 1 # Initialize the result to 1
for num in metadata['size']:
  n *= num
data = data.reindex(range(0,n),fill_value=0)
structure = [pandas.DataFrame({key:val for key,val in metadata['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in metadata['id']]
data.index = pandas.MultiIndex.from_product(structure,names=metadata['id'])
mydata1 = data.reset_index()
mydata1 = mydata1[mydata1.unit=='Thousand persons']
mydata1 = mydata1[mydata1.time=='2022']
mydata1 = mydata1[mydata1.sex=='Total']
mydata1 = mydata1[mydata1.age=='From 20 to 64 years']
mydata1 = mydata1[['geo',0]]
mydata1.rename(columns={0:'Thousand persons'},inplace=True)
mydata1.rename(columns={'geo':'ADMIN'},inplace=True)

mydata = mydata1.merge(mydata0,on='ADMIN',how='inner')
mydata['Percentage'] = 100*mydata['Migrants']/(1000*mydata['Thousand persons'])
mydata = mydara[['ADMIN','Percentage']]

world = geopandas.read_file('/content/drive/MyDrive/2024-HRM/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]
polygon = Polygon([(-25,35),(40,35),(40,75),(-25,75)])
europe = geopandas.clip(world,polygon)

mydata = mydata.merge(europe,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(10,15))
mydata.plot(column='Percentage',alpha=0.8,cmap='viridis',ax=ax,legend=True)
