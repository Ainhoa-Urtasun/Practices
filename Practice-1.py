import requests
import json
import pandas

def statistics(id,country):
  fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
  url = '{}{}'.format(fixed,id)
  data = requests.get(url).json()
  print(data)
  df = pandas.Series(data['value']).rename(index=int).sort_index()
  print(df)
  result = 1 # Initialize the result to 1
  for num in data['size']:
    result *= num
  v = v.reindex(range(0,result),fill_value=0)
  dimensions = [pandas.DataFrame({key:val for key,val in data['dimension'][dim]['category'].items()}).sort_values('index')['label'].values for dim in data['id']]
  v.index = pandas.MultiIndex.from_product(dimensions,names=data['id'])
  v.unstack('geo')[[country]]
