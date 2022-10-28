import json
import statistics

class DataStreamline:
    def __init__(self):
        ow_file = open("openweather.json")
        ow_data = json.load(ow_file)
        sh_file = open("surf_height.json")
        sh_data = json.load(sh_file)
        sq_file = open('surf_quality.json')
        sq_data = json.load(sq_file)
        with open('seatemp_cels.txt', 'r') as seatemp:
            sea_temp = seatemp.read()
        ow_code_file = open('ow_code_d.json')
        ow_code_data = json.load(ow_code_file)  # 0 = poor 10 = good
        wave_file = open('wavedata.json')
        wave_data = json.load(wave_file)


        def current_day_average(dict):
            dict_keys = dict.keys()
            today = list(dict_keys)[0]
            length = len(dict[today])
            sum = 0
            for value in dict[today]:
                sum += float(value)
            average = sum / length
            return average


        def current_day_max(dict):
            dict_keys = dict.keys()
            today = list(dict_keys)[0]
            return max(dict[today])


        def current_day_median(dict):
            dict_keys = dict.keys()
            today = list(dict_keys)[0]
            data_lst = dict[today]
            float_lst = []
            for num in data_lst:
                float_lst.append(float(num))
            return statistics.median(float_lst)


        def current_day_mode(dict):
            dict_keys = dict.keys()
            today = list(dict_keys)[0]
            data_lst = dict[today]
            float_lst = []
            for num in data_lst:
                float_lst.append(float(num))
            return statistics.mode(float_lst)


        def best_surf_selector(surf_quality_lst,
                               surf_height_lst):  # selects the best quality surf from the locations provided and returns quality and height of that location
            best_surf_loc = 'Bournemouth'
            surf_score = surf_quality_lst[0]['Bournemouth']
            for key in surf_quality_lst[0].keys():
                if surf_quality_lst[0][key] < surf_score:
                    best_surf_loc = key
            height = surf_height_lst[0][best_surf_loc]
            score = surf_score
            return score, height


        day_weather_code = current_day_mode(ow_data['weath_code'])
        day_temperature = current_day_max(ow_data['temp_C'])
        day_wind_speed = current_day_median(ow_data['wind_speed_m/s'])
        day_wind_deg = current_day_median(ow_data['wind_direction_deg'])
        day_cloud_cover = current_day_average(ow_data['cloud_cover_%'])
        day_surf_score, day_surf_height = best_surf_selector(sq_data, sh_data)
        day_swell = current_day_median(wave_data)
        day_weather_rating = ow_code_data[str(int(day_weather_code))][-1]

        suitable_sea_day_input = day_swell, int(day_surf_height[0]), day_surf_score, float(
            sea_temp), day_weather_rating, day_wind_speed, \
                                 day_wind_deg, float(day_temperature), day_cloud_cover

        with open('ocean_data_input_final', 'w') as f:
            f.write(str(suitable_sea_day_input))

        suitable_land_day_input = float(day_temperature), day_wind_speed, day_cloud_cover, day_weather_rating

        with open('land_data_input_final', 'w') as f:
            f.write(str(suitable_land_day_input))
            
DataStreamline()

