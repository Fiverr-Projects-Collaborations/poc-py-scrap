import requests
import pandas as pd
from pandas import ExcelWriter

data = {'url': [],
        'title': [],
        'rank': []}
df = pd.DataFrame(data)
headers = {'X-SEBITES-KEY': 'ABC'}
params = {'q': 'site:in.linkedin.com food snacks import india', 'limit': 200, 'gl': 'IN'}
x = requests.get('https://api.sebites.com/gs/search-results', headers=headers, params=params)
data = x.json()['results']['organic_results']

for link in data:
    new_row = link
    #print(link)
    df = df.append(link, ignore_index=True)
writer = ExcelWriter('SnacksImporters.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
#print(df)
