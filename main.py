from datetime import datetime
from operator import index
from re import I, M
from statistics import mean
from openweather_api import OpenWeatherAPI
from wave_scrape import Combine, WaveScrape
from sea_temp import SeaTemp
from postcode_coords import PostCode
import requests
import json
from cmath import inf
from math import sqrt as root
from cycle import Cycle


input_post_code = input('Enter Postcode: ')

pcode = PostCode()
coords = pcode.postcode_to_coord(input_post_code)
closest_beach = pcode.closest_beach(coords, pcode.surf_loc_data)
beach_surfline_id = closest_beach['_id']
beach_name = closest_beach['name']

ow_d = OpenWeatherAPI.format_d(
    OpenWeatherAPI(coords_dict=coords).weather_dict())
ocean_weather_d = Combine().run(beach_surfline_id)

sunrise, sunset = OpenWeatherAPI(coords_dict=coords).daylight()


# returns the weather rating 0-10 greater value indicates more favourable weather conditions.
def code_to_score(ow_code):
    ow_code_d = {"200": ["Thunderstorm", "thunderstorm with light rain", 1],
                 "201": ["Thunderstorm", "thunderstorm with rain", 1],
                 "202": ["Thunderstorm", "thunderstorm with heavy rain", 0],
                 "210": ["Thunderstorm", "light thunderstorm", 1],
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
                 "522": ["Rain", "heavy intensity shower rain", 3],
                 "531": ["Rain", "ragged shower rain", 3],
                 "600": ["Snow", "light snow", 3],
                 "601": ["Snow", "Snow", 1],
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
                 "802": ["Clouds", "scattered clouds: 25-50%", 7],
                 "803": ["Clouds", "broken clouds: 51-84%", 8],
                 "804": ["Clouds", "overcast clouds: 85-100%", 8]}

    return int(ow_code_d[str(ow_code)][-1])


def K_to_C(kelvin_temp):
    return kelvin_temp - 273.15


def unix_to_time(unix):
    dt = datetime.fromtimestamp(unix)
    return dt.time()


# if time input is within daylight returns TRUE.
def daylight_check(unix_time):
    if unix_to_time(sunrise) <= unix_to_time(unix_time) <= unix_to_time(sunset):
        return True
    else:
        return False


def weather_check(weather, activity):
    if activity['temp'][0] <= K_to_C(weather['temp']) <= activity['temp'][-1]:
        if activity['weather_score'][0] <= code_to_score(weather['weather_id']) <= activity['weather_score'][-1]:
            if activity['cloud_cover'][0] <= weather['clouds'] <= activity['cloud_cover'][-1]:
                if activity['visibility'][0] <= weather['visibility'] <= activity['visibility'][-1]:
                    if activity['wind'][0] <= weather['wind_speed'] <= activity['wind'][-1]:
                        if activity['gust'][0] <= weather['wind_gust'] <= activity['gust'][-1]:
                            return True


# def weather_check_ocean(weather, ocean_weather, activity):
#     if activity

# TODO   create more land based activities (climbing, hiking, sunbathing, golf), setup link to app? save data somewhere.


def activity_weather_check(openweatherAPI_dict, activity_info):
    time_lst = list(openweatherAPI_dict.keys())
    time_segments = 0
    suitable_weather_streak = {}
    for unix_key in openweatherAPI_dict.keys():
        if daylight_check(unix_key):
            if weather_check(weather=openweatherAPI_dict[unix_key], activity=activity_info):
                time_segments += 1
            else:
                if time_segments >= 2:
                    suitable_weather_streak[unix_key] = time_segments
                    time_segments = 0
        else:
            if time_segments >= 2:
                suitable_weather_streak[unix_key] = time_segments
                time_segments = 0

    lst = []

    for time, data_points in suitable_weather_streak.items():
        end_of_window = time
        index = time_lst.index(time)
        start_of_window = time_lst[index - data_points]

        lst.append((start_of_window, end_of_window))
    lst.insert(0, activity_info['name'])

    return lst

def ocean_keys(index: int, ow_keys: list, ocean_keys: list):
    return_lst = []
    start_time = ow_keys[index]
    end_time = ow_keys[index + 1]
    for time in ocean_keys:
        if start_time <= time <= end_time:
            return_lst.append(time)
    return return_lst


def weather_check_land(weather, activity):
    if activity['temp'][0] <= K_to_C(weather['temp']) <= activity['temp'][-1]:
        if activity['weather_score'][0] <= code_to_score(weather['weather_id']) <= activity['weather_score'][-1]:
            if activity['cloud_cover'][0] <= weather['clouds'] <= activity['cloud_cover'][-1]:
                if activity['visibility'][0] <= weather['visibility'] <= activity['visibility'][-1]:
                    return True    


def ocean_activity_check(weather, activity): ## TODO
    if activity['surf_height'][0] <=  weather['surf']['raw']['max'] <= activity['surf_height'][1]:
        if weather['directionType'] in activity['wind_dir']:
            pass

## TODO FINISH ABOVE CODE /////////////////////////////////////////////////////////////////////////////////


def ocean_activity_weather_check(openweatherAPI_dict, ocean_forecast, activity_info): ##TODO
    ow_timestamps = list(openweatherAPI_dict.keys())
    ocean_timestamps = list(ocean_forecast.keys())
    ow_period_count = 0

    for index in len(ow_timestamps):
        if daylight_check(ow_timestamps[index]):  # daylight check
            if weather_check_land(weather=openweatherAPI_dict[ow_timestamps[index]], activity=activity_info['land']):
                if (index + 1) > len(ow_timestamps):  # Stops error if last timestamp
                    return False
                else:
                    ocean_keys_lst = ocean_keys(index=index, ow_keys=ow_timestamps, ocean_keys=ocean_timestamps) #gives oceankeys within both timestamps
                    for key in ocean_keys_lst:
                        if not ocean_activity_check(ocean_weather=ocean_forecast[key], activity=activity_info['surf']): ## TODO
                            break
                        ow_period_count += 1


def unix_to_dt(unix_time):
    return datetime.fromtimestamp(unix_time)


def time_period_printer(suitable_time_lst):
    if len(suitable_time_lst) > 1:
        print(suitable_time_lst[0])
        for time in suitable_time_lst[1:]:
            print('start: ' + str(unix_to_dt(time[0])))
            print('end:   ' + str(unix_to_dt(time[1])))


for sport in Cycle.sport_lst:
    suitable_time = activity_weather_check(ow_d, sport)
    time_period_printer(suitable_time_lst=suitable_time)
