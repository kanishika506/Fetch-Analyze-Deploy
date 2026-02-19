import requests 
import pandas as pd
url="https://api.open-meteo.com/v1/forecast"
d={"latitude": 51.5074,
   "longitude": -0.1278,
   "hourly": "temperature_2m"
   }
response=requests.get(url, params=d)
data=response.json()
av=data["hourly"]
df=pd.DataFrame(av)
df.to_csv("london_weather.csv",index=False)

print(df)