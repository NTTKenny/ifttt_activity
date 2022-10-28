import datetime
import datetime as dt
import requests
import json
from datetime import timedelta

class OpenWeatherApi:
    def __init__(self):

        API_key = 'f4c16045c21419f2605536881085186b'
        city = 'Bournemouth'
        base_url = 'http://api.openweathermap.org/data/2.5/forecast?'

        url = base_url + "appid=" + API_key + '&q=' + city

        response = requests.get(url).json()

        # print(response)

        weather_data = response['list']

        today_date = datetime.date.today()


        def unix_to_std_time(unix_time):  # returns standard time format from unix time.
            date_time = dt.datetime.fromtimestamp(unix_time)
            formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')  # converts date to string not needed atm
            return date_time


        #
        # for dict in weather_data:
        #     date_lst = (dict['dt_txt'])


        def time_within_daylight(unix_time):  # returns True/False if weather timestamp is within daylight
            sunrise_time = unix_to_std_time(response['city']['sunrise'])
            sunset_time = unix_to_std_time(response['city']['sunset'])
            tme = unix_to_std_time(unix_time)
            if sunset_time.time() > tme.time() > sunrise_time.time():
                return True
            else:
                return False


        def text_day_5():  # returns a list of the next 5 days in text format.
            text_day_lst = []
            for number in range(0, 6):
                future_date = today_date + datetime.timedelta(days=number)
                future_date_text = future_date.strftime('%A')
                text_day_lst.append(future_date_text)
            return text_day_lst


        def data_reformatting_2i(sorted_weather_dict_by_day, index_1, index_2=None):
            w_d = sorted_weather_dict_by_day
            d = {}
            day_lst = text_day_5()
            for day_ in day_lst:
                d[day_] = []
            for day in w_d.keys():
                for data_snap in w_d[day]:
                    d[day].append(data_snap[index_1][index_2])
            return d


        def data_reformatting_1i(sorted_weather_dict_by_day, index_1):
            w_d = sorted_weather_dict_by_day
            d = {}
            day_lst = text_day_5()
            for day_ in day_lst:
                d[day_] = []
            for day in w_d.keys():
                for data_snap in w_d[day]:
                    d[day].append(data_snap[index_1])
            return d


        def weather_sorted_by_day_light(open_weather_lst):  # Puts data into a dict by day if it is within daylight time.
            daylight_raw = []
            days = text_day_5()
            date = [today_date + timedelta(days=num) for num in range(0, 6)]
            date_day_dict = {}
            return_dict = {}
            for day in days:
                return_dict[day] = []
            for i in range(0, 6):
                date_day_dict[date[i].day] = days[i]
            for dic in open_weather_lst:
                if time_within_daylight(dic['dt']):
                    daylight_raw.append(dic)
            for daylight_dic in daylight_raw:
                time = unix_to_std_time(daylight_dic['dt'])
                return_dict[date_day_dict[time.day]].append(daylight_dic)
            return  return_dict


        day_light_weather_d = weather_sorted_by_day_light(weather_data)


        finished_dict = {}

        finished_dict["temp_C"] = data_reformatting_2i(day_light_weather_d, 'main', 'temp_max')
        finished_dict["wind_speed_m/s"] = data_reformatting_2i(day_light_weather_d, 'wind', 'speed')
        finished_dict["wind_direction_deg"] = data_reformatting_2i(day_light_weather_d, 'wind', 'deg')
        finished_dict["cloud_cover_%"] = data_reformatting_2i(day_light_weather_d, 'clouds', 'all')
        finished_dict["time"] = data_reformatting_1i(day_light_weather_d, 'dt_txt')
        finished_dict['weath_code'] = data_reformatting_1i(day_light_weather_d, 'weather')





        def kelvin_to_c_in_dict(dict):
            for key in dict.keys():
                temp_lst = []
                for temp in dict[key]:
                    converted_temp = temp -273.15
                    temp_lst.append("{:.2f}".format(converted_temp))
                dict[key] = temp_lst
            return dict


        finished_dict['temp_C'] = kelvin_to_c_in_dict(finished_dict['temp_C'])


        def weather_code_only(dict):
            for day in dict.keys():
                temp_lst = []
                for lst in dict[day]:
                    for lst_1 in lst:
                     temp_lst.append(lst_1['id'])
                dict[day] = temp_lst
            return dict

        finished_dict['weath_code'] = weather_code_only(finished_dict['weath_code'])

        with open("openweather.json", "w") as f:
            json.dump(finished_dict, f)


OpenWeatherApi()
