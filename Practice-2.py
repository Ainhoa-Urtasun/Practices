import requests
import json
import pandas

def statistics(treelabel,country,unit,Total):
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
  data = data.unstack(['geo'])[[country]].reset_index()
  data = data[data.unit==unit]
  data['time'] = data['time'].astype(int)
  data = data[data.time>2009]
  data = data[(data.age=='From 15 to 24 years')|(data.age=='From 25 to 54 years')|(data.age=='From 55 to 64')]
  data = data[['age','sex','time',country]]
  return data
