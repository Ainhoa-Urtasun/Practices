import requests
import json
import pandas

fixed = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
datasetCode = 'qoe_ewcs_7b3'
url = '{}{}'.format(fixed,datasetCode)
data = requests.get(url).json()
