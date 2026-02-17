import requests

url="https://rickandmortyapi.com/api/character"

d={
    "name":"morty", 
    
    "status":"dead"
}

response=requests.get(url, params=d)
data=response.json()
#task=> get species of first character in result 
print(data['results'][0]['species'])