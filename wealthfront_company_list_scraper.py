import requests
import pandas as pd
from pandas.io.json import json_normalize

url = 'https://blog.wealthfront.com/wp-content/themes/wealthfront-chisel/career-launching-companies/career-launching-companies.json'
r = requests.get(url=url)

companies_list = pd.read_json(path_or_buf=url, orient='records')
df = json_normalize(r.json()['companies'])
df.to_csv('2019_wealthfront_career_launching_list.csv')