aimport requests
import json
import pandas

def statistics(treelabel,country):
  fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
  url = '{}{}'.format(fixed,treelabel)
  metadata = requests.get(url).json()
  print(metadata)
  print(metadata['id'])
  print(metadata['value'])
  data = pandas.Series(metadata['value']).rename(index=int).sort_index()
  print(data)
  result = 1 # Initialize the result to 1
  for num in metadata['size']:
    n *= num
  data = data.reindex(range(0,n),fill_value=0)
  structure = [pandas.DataFrame({key:val for key,val in metadata['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in metadata['id']]
  data.index = pandas.MultiIndex.from_product(dimensions,names=metadata['id'])
  v.unstack('geo')[[country]]
