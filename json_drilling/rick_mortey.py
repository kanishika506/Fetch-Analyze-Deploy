import requests

url="https://rickandmortyapi.com/api/character"

response=requests.get(url)
if response.status_code==200:
    data=response.json()

    characters=data['results']
    print(f"--Total characters found in this page: {len(characters)}\n")

    for i in range(3):
        char=characters[i]
        name=char['name']
        status=char['status']
        origin_name=char['origin']['name']

        print(f"{i+1}. Name:{name}")
        print(f" status:{status}")
        print(f"origin:{origin_name}\n")
else:
    print(f"Failed! source code:{response.status_code}")