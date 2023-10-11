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
url = '{}{}'.format(fixed,'isoc_e_diin2')
metadata = requests.get(url).json()
print(metadata['label'])
data = pandas.Series(metadata['value']).rename(index=int).sort_index()
n = 1 # Initialize the result to 1
for num in metadata['size']:
  n *= num
data = data.reindex(range(0,n),fill_value=0)
structure = [pandas.DataFrame({key:val for key,val in metadata['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in metadata['id']]
data.index = pandas.MultiIndex.from_product(structure,names=metadata['id'])
mydata = data.reset_index()
mydata = mydata[mydata.time=='2022']
mydata = mydata[mydata.industry=='Professional, scientific and technical activities']
mydata = mydata[mydata['digital intensity'].str.contains('Enterprises with very high digital intensity')]
mydata = mydata[['geo',0]]
mydata.rename(columns={0:'Percentage'},inplace=True)
mydata.rename(columns={'geo':'ADMIN'},inplace=True)

world = geopandas.read_file('/content/drive/MyDrive/2024-HRM/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]
polygon = Polygon([(-25,35),(40,35),(40,75),(-25,75)])
europe = geopandas.clip(world,polygon)

mydata = mydata.merge(europe,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(10,15))
mydata.plot(column='Percentage',alpha=0.8,cmap='viridis',ax=ax,legend=True)
ax.set_title('Percentage of professional, scientific, and technical businesses\nwith very high digital intensity in 2022 (source: Eurostat)')
ax.axis('off')
