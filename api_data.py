import requests as api
api_key ="YOUR_API_KEY"  #OPENWEATHERMAP
class Weather_Data():
    def __init__(self,city,unit):
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}"
        self.response = api.get(self.url)
        self.weather = self.response.json()
    def temp(self):
        self.temperature = self.weather["main"]["temp"]
        return self.temperature
    def atmosphere(self):
        self.atmos = self.weather["weather"][0]["description"]
        return self.atmos
