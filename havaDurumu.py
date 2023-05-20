import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == "404":
            print("Şehir bulunamadı!")
            return

        # Hava durumu bilgilerini al
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Bilgileri yazdır
        print(f"Hava Durumu: {weather}")
        print(f"Sıcaklık: {temperature}°C")
        print(f"Nem: {humidity}%")
        print(f"Rüzgar Hızı: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("Hata: ", e)

# API anahtarınızı ve hava durumunu almak istediğiniz şehiri girin
api_key = str(input("API anahtarınızı giriniz: "))
city = str(input("şehir ismi giriniz: "))

get_weather(api_key, city)
