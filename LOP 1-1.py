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
url = '{}{}'.format(fixed,'lfso_21jsat01')
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
mydata = mydata[mydata.sex=='Total']
mydata = mydata[mydata['c_birth']=='Total']
mydata = mydata[mydata['isced11']=='All ISCED 2011 levels']
mydata = mydata[mydata.age=='From 25 to 74 years']
mydata = mydata[(mydata['lev_satis']=='Total')|(mydata['lev_satis']=='High')]
mydata = mydata[['geo','lev_satis',0]]
mydata.rename(columns={'geo':'ADMIN'},inplace=True)
mydata.rename(columns={0:'Thousand persons'},inplace=True)
mydata = mydata.pivot(index='ADMIN',columns='lev_satis',values='Thousand persons').reset_index()
# mydata.rename(columns={'ADMIN':'GEO'},inplace=True)
# mydata = mydata.rename_axis(columns=None)
mydata['percentage'] = 100*mydata['High']/mydata['Total']
table = mydata[['ADMIN','percentage']]

world = geopandas.read_file('/content/LOP/ne_110m_admin_0_countries.zip')[['ADMIN','geometry']]
polygon = Polygon([(-25,35),(40,35),(40,75),(-25,75)])
europe = geopandas.clip(world,polygon)

mydata = mydata.merge(europe,on='ADMIN',how='right')
mydata = geopandas.GeoDataFrame(mydata,geometry='geometry')
fig,ax = plt.subplots(1,figsize=(10,10))
mydata.plot(column='percentage',alpha=0.8,cmap='cool',ax=ax,legend=True)
ax.set_title('Percentage of employees from 25 to 74 years\nhighly satisfied with their job in 2021 (source: Eurostat)')
ax.axis('off')
