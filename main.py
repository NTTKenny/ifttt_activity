from datetime import datetime
import ocean_activity
from postcode_coords import PostCode
from openweather_api import OpenWeatherAPI as ow_api
from wave_scrape import OceanWeather
from land_activity import LandSport
from sea_temp import SeaTemp

# assigned variables.
ocean_keys_land = ['temp', 'cloud_cover', 'weather_score', 'visibility']
ocean_keys_ocean = ['surf_max', 'surf_min', 'windGust',
                    'wind_speed', 'rating_value', 'directionType']
land_keys = ['temp', 'weather_score',
             'cloud_cover', 'visibility', 'wind', 'gust']
activity_list = [LandSport.mountain_biking]
ocean_activity_list = [ocean_activity.OceanSport.surfing,
                       ocean_activity.OceanSport.paddle_boarding, ocean_activity.OceanSport.wild_sea_swimming]

# user input.
user_postcode = input('Enter postcode of desired activity location: ')

# location data from user input.
postcode = PostCode()
co_ords = postcode.postcode_to_coord(user_postcode)
beach = postcode.closest_beach(co_ords, postcode.surf_loc_data)
beach_id = beach['_id']
beach_name = beach['name']
sunrise, sunset = ow_api(coords_dict=co_ords).daylight()

# weather data.
ow = ow_api(coords_dict=co_ords).weather_dict()
forecast = ow_api.format_d(d=ow)
forecast_keys = list(forecast.keys())
beach_forecast = OceanWeather().run(beach_id)
sea_temp = float(SeaTemp().sea_temp_c)


# Functions.
def unix_to_time(unix):
    date_time = datetime.fromtimestamp(unix)
    time = date_time.time()
    return time


# if input timestamp is within global sunrise, sunset times, returns True.
def daylight_check(unix):
    if unix_to_time(sunrise) <= unix_to_time(unix) <= unix_to_time(sunset):
        return True
    else:
        return False


def forecast_check(weather, activity, paramater_list):
    def parameter_check(key):
        if activity[key][0] <= weather[key] <= activity[key][-1]:
            return True
        else:
            return False

    for parameter_key in (paramater_list):
        if not parameter_check(key=parameter_key):
            break
        return True


def start_end_consecutive_ints(index_list):
    saved_value = 0
    return_list = []
    count = 0
    for i, integer in enumerate(index_list):
        count = 0
        if integer < saved_value:
            continue

        if integer == index_list[-1]:
            if integer - 1 == index_list[-2]:
                return_list.append((index_list[-2], index_list[-1]))
                break

        for o, int in enumerate(index_list[i+1:]):

            starting_index = index_list.index(int)
            val = index_list[i+1:][o-1]
            if o + integer + 1 == int:
                count += 1

            else:
                if count >= 1:
                    return_list.append((integer, val))
                    saved_value = index_list[starting_index]
                    break
                else:
                    break

    return return_list


def activity_check(weather_forecast, activity_requirements, parameter):
    index_lst = []
    for i, (unix_time_key, timestamp_weather) in enumerate(weather_forecast.items()):
        if daylight_check(unix=unix_time_key):
            if forecast_check(weather=timestamp_weather, activity=activity_requirements, paramater_list=parameter):
                index_lst.append(i)

    return (index_lst)


def times_for_activity(activity_list, land_parameter_keys, ocean_parameter_keys=None, output_d=None):
    if output_d == None:
        output_d = {}

    for activity_requirement_values in activity_list:
        activity_time_windows = []
        suitable_times_index = activity_check(
            weather_forecast=forecast, activity_requirements=activity_requirement_values, parameter=land_parameter_keys)
        suitable_windows_index = start_end_consecutive_ints(
            suitable_times_index)
        if ocean_parameter_keys != None:
            for (start, end) in suitable_windows_index:
                print(start, end)
                oww = [value for value in list(beach_forecast.keys(
                )) if forecast_keys[start] <= value <= forecast_keys[end]]
                for time in oww:
                    if forecast_check(beach_forecast[time], activity=activity_requirement_values, paramater_list=ocean_keys_ocean):
                        if activity_requirement_values['sea_temp_min'] <= sea_temp:
                            if time == oww[-1]:
                                start_timestamp = datetime.fromtimestamp(
                                    forecast_keys[start])
                                end_timestamp = datetime.fromtimestamp(
                                    forecast_keys[end])
                                activity_time_windows.append(
                                    (start_timestamp, end_timestamp))
                                output_d[activity_requirement_values['name']
                                         ] = activity_time_windows

                    else:
                        break
        else:
            for (start, end) in suitable_windows_index:
                start_timestamp = datetime.fromtimestamp(forecast_keys[start])
                end_timestamp = datetime.fromtimestamp(forecast_keys[end])
                activity_time_windows.append((start_timestamp, end_timestamp))
                output_d[activity_requirement_values['name']
                         ] = activity_time_windows

    return output_d


land_activity_times = (times_for_activity(
    activity_list=activity_list, land_parameter_keys=land_keys))
all_activity_times = (times_for_activity(activity_list=ocean_activity_list,
                                         land_parameter_keys=ocean_keys_land, ocean_parameter_keys=ocean_keys_ocean, output_d=land_activity_times))

ifttt_output = {}
for key, value in all_activity_times.items():
    if len(value) > 0:
        s, e = value[0]
        start = s.strftime('%A %R:')
        end = e.strftime('%R:')
        ifttt_output[key] = f"{start} until {end}"

print(ifttt_output)
