import requests

city=input("Enter the Name of the City: ")

response=requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")

if response.status_code==200:
    data=(response.json())
    if not data.get("results"):
        print("City not Found.")
    else:    
        lat= data["results"][0]["latitude"] 
        lon= data["results"][0]["longitude"]
        print(f'Latitude: {lat},Longitude:{lon}')

        weather_response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

        if weather_response.status_code==200:
            data=(weather_response.json())   
            temperature=data["current_weather"]["temperature"]
            print(f"Weather of {city} is {temperature}°C")
        else:
            print("Error Occured, Try again")


else:
    print("Error Occured, Try again")