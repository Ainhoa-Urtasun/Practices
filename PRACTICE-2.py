import requests
import json
import pandas
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pyproj
import warnings
warnings.filterwarnings("ignore")

#plt.rcParams['figure.figsize']=(12,10)
#plt.rcParams['font.size']=12

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
data = data.reset_index()
data['time'] = data['time'].astype(int)
data = data[data.time>2009]
data = data[data.age=='From 25 to 54 years']
data = data[['sex','time',0]]
data.rename(columns={0:'Thousand persons'},inplace=True)

world = geopandas.read_file('/content/drive/MyDrive/2024-HRM/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]
polygon = Polygon([(-25,35),(40,35),(40,75),(-25,75)])
europe = geopandas.clip(world,polygon)

data.rename(columns={'geo':'ADMIN'},inplace=True)
mydata = data.copy()
mydata = mydata.merge(europe,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(10,15))
mydata.plot(column='percentage',alpha=0.8,cmap='viridis',ax=ax,legend=True)
