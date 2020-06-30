import requests
place_list = [
(33.746855, -84.387692, "Atlanta, GA"),
(30.238233, -97.753415, "Austin, TX"),
(37.774785, -122.419238, "San Francisco, CA"),
(34.161818, -106.245270, "")]

def get_weather_data(locations):
    weather_data_save_packet = {}
    for location in locations:
        url = "https://api.climacell.co/v3/weather/realtime"
        payload = {"apikey":
        "qMN1wQdh97S3QBrGGV90kKUSNTUI46l8",
        "lat":location[0],
        "lon":location[1],
        "fields":
        ["temp", 
        "precipitation", 
        "wind_gust"
        ],
        "unit_system":"us",
        }

        response  = requests.get(url, params=payload).json()
        weather_data_save_packet[location[2]] =  response["temp"]["value"]
    return weather_data_save_packet


weather_data = get_weather_data(place_list)
print(weather_data)