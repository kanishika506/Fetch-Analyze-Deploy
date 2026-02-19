#data
data={
  "region": "Europe",
  "stations": [
    {
      "station_id": "LDN-01",
      "city": "London",
      "readings": [
        {"timestamp": "10:00", "temp": 15, "humidity": 80},
        {"timestamp": "11:00", "temp": 17, "humidity": 75}
      ]
    },
    {
      "station_id": "PAR-02",
      "city": "Paris",
      "readings": [
        {"timestamp": "10:00", "temp": 19, "humidity": 60}
      ]
    }
  ]
}

#get 2nd temp reading of london

print(f"second reading temperatue  in london:{data['stations'][0]['readings'][1]['temp']}\n")
#get humidity of paris
print(f"humidity of paris:{data['stations'][1]['readings'][0]['humidity']}\n")