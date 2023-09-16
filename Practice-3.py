import requests
import json
import pandas

def data(treelabel,industry,country1,country2,country3,unit):
  fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
  url = '{}{}'.format(fixed,treelabel)
  metadata = requests.get(url).json()
  print(metadata['label'])
  data = pandas.Series(metadata['value']).rename(index=int).sort_index()
  n = 1 # Initialize the result to 1
  for num in metadata['size']:
    n *= num
  data = data.reindex(range(0,n),fill_value=0)
  structure = [pandas.DataFrame({key:val for key,val in metadata['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in metadata['id']]
  data.index = pandas.MultiIndex.from_product(structure,names=metadata['id'])
  data = data.reset_index()
  data = data[data['nace_r2']=='Professional, scientific and technical activities']
  data = data[(data.geo==country1)|(data.geo==country2)|(data.geo==country3)]
  data = data[data['indic_is']==unit]
  data['time'] = data['time'].astype(int)
  data = data[data.time==2022]
  return data
