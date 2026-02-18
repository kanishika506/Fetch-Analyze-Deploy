import requests 
import pandas as pd
url="https://rickandmortyapi.com/api/character" 
all_dead=[]
next_page="https://rickandmortyapi.com/api/character?name=morty&status=dead"
while next_page:
    response=requests.get(next_page)
    data=response.json()
    all_dead.extend(data['results'])
    next_page=data['info']['next']
print(f"total morty dead characters:{len(all_dead)}")

df=pd.DataFrame(all_dead)
df=df[['name'],['status'],['species'],['gender']]
df.to_csv("morty_dead_char.csv",index=False)
