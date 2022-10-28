import requests


class OpenWeatherAPI:
    def __init__(self, coords_dict):
        self.coords_dict = coords_dict

    def k_to_c(kelvin_temp):
        celsius = kelvin_temp - 273.15
        return celsius
    
    def ms_to_mph(meters_second):
         mph = meters_second * 2.23694
         return mph

    def weather_rating(ow_api_code):
        code_dict = {"200": ["Thunderstorm", "thunderstorm with light rain", 0],
                 "201": ["Thunderstorm", "thunderstorm with rain", 0],
                 "202": ["Thunderstorm", "thunderstorm with heavy rain", 0],
                 "210": ["Thunderstorm", "light thunderstorm", 0],
                 "211": ["Thunderstorm", "thunderstorm", 0],
                 "212": ["Thunderstorm", "heavy thunderstorm", 0],
                 "221": ["Thunderstorm", "ragged thunderstorm", 0],
                 "230": ["Thunderstorm", "thunderstorm with light drizzle", 0],
                 "231": ["Thunderstorm", "thunderstorm with drizzle", 0],
                 "232": ["Thunderstorm", "thunderstorm with heavy drizzle", 0],
                 "300": ["Drizzle", "light intensity drizzle", 3],
                 "301": ["Drizzle", "drizzle", 3],
                 "302": ["Drizzle", "heavy intensity drizzle", 2],
                 "310": ["Drizzle", "light intensity drizzle rain", 3],
                 "311": ["Drizzle", "drizzle rain", 3],
                 "312": ["Drizzle", "heavy intensity drizzle rain", 2],
                 "313": ["Drizzle", "shower rain and drizzle", 3],
                 "314": ["Drizzle", "heavy shower rain and drizzle", 2],
                 "321": ["Drizzle", "shower drizzle", 4],
                 "500": ["Rain", "light rain", 4],
                 "501": ["Rain", "moderate rain", 4],
                 "502": ["Rain", "heavy intensity rain", 3],
                 "503": ["Rain", "very heavy rain", 2],
                 "504": ["Rain", "extreme rain", 0],
                 "511": ["Rain", "freezing rain", 0],
                 "520": ["Rain", "light intensity shower rain", 4],
                 "521": ["Rain", "shower rain", 4],
                 "522": ["Rain", "heavy intensity shower rain", 2],
                 "531": ["Rain", "ragged shower rain", 3],
                 "600": ["Snow", "light snow", 0],
                 "601": ["Snow", "Snow", 0],
                 "602": ["Snow", "Heavy snow", 0],
                 "611": ["Snow", "Sleet", 0],
                 "612": ["Snow", "Light shower sleet", 1],
                 "613": ["Snow", "Shower sleet", 1],
                 "615": ["Snow", "Light rain and snow", 1],
                 "616": ["Snow", "Rain and snow", 1],
                 "620": ["Snow", "Light shower snow", 1],
                 "621": ["Snow", "Shower snow", 1],
                 "622": ["Snow", "Heavy shower snow", 0],
                 "701": ["Mist", "mist", 5],
                 "711": ["Smoke", "Smoke", 0],
                 "721": ["Haze", "Haze", 5],
                 "731": ["Dust", "sand/ dust whirls", 0],
                 "741": ["Fog", "fog", 5],
                 "751": ["Sand", "sand", 0],
                 "761": ["Dust", "dust", 4],
                 "762": ["Ash", "volcanic ash", 0],
                 "771": ["Squall", "squalls", 0],
                 "781": ["Tornado", "tornado", 0],
                 "800": ["Clear", "sky", 10],
                 "801": ["Clouds", "few clouds: 11-25%", 9],
                 "802": ["Clouds", "scattered clouds: 25-50%", 8],
                 "803": ["Clouds", "broken clouds: 51-84%", 7],
                 "804": ["Clouds", "overcast clouds: 85-100%",6]}
        rating = int(code_dict[str(ow_api_code)][-1])
        return rating

    def weather_dict(self):
        lat, lon = self.coords_dict['lat'], self.coords_dict['lon']

        api_key = 'f4c16045c21419f2605536881085186b'
        weather_url = 'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=' \
                    '{API_key}'.format(lat=lat, lon=lon, API_key=api_key)
        weather_dict = requests.get(weather_url).json()['list']

        d = {}

        for dict in weather_dict:
            u_time = dict.pop('dt')
            d[u_time] = dict
        
        return d

    def format_d(d):
        ow_api = {}
        for key in d.keys():
            ow_api[key] = {'timestamp': key, 'temp': OpenWeatherAPI.k_to_c(d[key]['main']['temp']), 'humidity': d[key]['main']['humidity'], 'weather_score': OpenWeatherAPI.weather_rating(d[key]['weather'][0]['id']), 'weather_desc': d[key]['weather'][0]['description'], 'cloud_cover': d[key]['clouds']['all'], 'wind': OpenWeatherAPI.ms_to_mph(d[key]['wind']['speed']), 'gust': OpenWeatherAPI.ms_to_mph(d[key]['wind']['gust']), 'visibility': d[key]['visibility']}
        return ow_api


    def daylight(self): # returns tuple of unix sunrise, sunset.
        lat, lon = self.coords_dict['lat'], self.coords_dict['lon']

        api_key = 'f4c16045c21419f2605536881085186b'
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=' \
                    '{API_key}'.format(lat=lat, lon=lon, API_key=api_key)
        weather = requests.get(weather_url).json()

        sun_rise_set = (weather['sys']['sunrise'], weather['sys']['sunset'])

        return sun_rise_set