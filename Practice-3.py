import requests
import json
import pandas

def data(treelabel,industry,country1,country2):
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
  data = data[data['indic_is'].str.contains('Version 4')]
  data = data[data['nace_r2']==industry]
  data = data[(data.geo==country1)|(data.geo==country2)]
  data['time'] = data['time'].astype(int)
  data = data[data.time==2022]
  data = data[['size_emp','nace_r2','geo','time','indic_is',0]]
  data.rename(columns={'size_emp':'size','nace_r2':'industry','indic_is':'digital intensity',0:'percentage of enterprises'},inplace=True)
  return data
