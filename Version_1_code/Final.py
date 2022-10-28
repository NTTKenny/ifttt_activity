class Final:
    def __init__(self):
        class LandActivity:
            def __init__(self, activity_name, temp_range, wind_speed, weather_score, cloud_cover):
                self.cloud_cover = cloud_cover
                self.weather_score = weather_score
                self.temp_range = temp_range
                self.wind_speed = wind_speed
                self.activity_name = activity_name

            def suitable_land_day(self, day_air_temp, day_wind_speed, day_cloud_cover, day_weather_quality):
                if self.temp_range[0] < day_air_temp < self.temp_range[-1]:
                    if self.wind_speed[0] < day_wind_speed < self.wind_speed[-1]:
                        if self.cloud_cover[0] < day_cloud_cover < self.cloud_cover[-1]:
                            if self.weather_score[0] <= day_weather_quality <= self.weather_score[-1]:
                                days_activity_options.append(self.activity_name)


        class OceanActivity:
            def __init__(self, wave_height, surf_height, wave_quality, sea_temperature, weather_quality, wind_speed,
                         wind_direction,
                         temperature, cloud_cover, name):
                self.surf_height = surf_height
                self.temperature = temperature
                self.wind_speed = wind_speed
                self.weather_quality = weather_quality
                self.sea_temperature = sea_temperature
                self.wave_quality = wave_quality
                self.wave_height = wave_height
                self.wind_direction = wind_direction
                self.cloud_cover = cloud_cover
                self.name = name

            def suitable_sea_day(self, t_wave_height, t_surf_height, t_wave_quality, t_sea_temperature, t_weather_score,
                                 t_wind_speed,
                                 t_wind_direction, t_temperature, t_cloud_cover):
                if self.wave_height[0] < t_wave_height < self.wave_height[-1]:
                    if self.surf_height[0] <= t_surf_height <= self.surf_height[-1]:
                        if self.wave_quality[0] <= t_wave_quality <= self.wave_quality[-1]:
                            if self.sea_temperature[0] < t_sea_temperature < self.sea_temperature[-1]:
                                if self.weather_quality[0] <= t_weather_score <= self.weather_quality[-1]:
                                    if self.wind_speed[0] < t_wind_speed < self.wind_speed[-1]:
                                        if self.wind_direction[0] < t_wind_direction < self.wind_direction[-1]:
                                            if self.temperature[0] < t_temperature < self.temperature[-1]:
                                                if self.cloud_cover[0] < t_cloud_cover < self.cloud_cover[-1]:
                                                    days_activity_options.append(self.name)


        days_activity_options = []

        sup = OceanActivity([0, 0.13], [0, 2], [0, 999], [12, 999], [5, 999], [0, 4],
                            [0, 999], [18, 999], [0, 80], "Stand Up Paddleboarding")
        surf = OceanActivity([0, 999], [2, 10], [5, 10], [10, 999], [3, 999],
                             [0, 10], [0, 999], [12, 999], [0, 999], 'Surfing')
        body_board = OceanActivity([0.3, 2.5], [3, 14], [0, 999], [12, 999], [3, 10], [0, 10],
                                   [0, 999], [13, 999], [0, 999], 'Body Boarding')
        swimming = OceanActivity([0, 0.35], [0, 3], [0, 999], [14, 999], [4, 999], [0, 6],
                                 [0, 999], [14, 999], [0, 999], 'Ocean Swimming')
        kite_boarding = OceanActivity([0, 999], [0, 5], [7, 13], [10, 999], [3, 999],
                                      [0, 10], [90, 270], [12, 999], [0, 999], 'Kite Boarding')
        wing_surf = OceanActivity([0, 999], [0, 5], [7, 13], [10, 999], [3, 999],
                                  [0, 10], [90, 270], [12, 999], [0, 999], 'Wing Surfing')
        # test = OceanActivity([0, 100], [0, 100], [0, 100], [0, 100], [0, 100], [0, 100], [0, 300], [0, 100], [0, 100], 'Test')

        indoor_climbing = LandActivity("Indoor Climbing", [0, 22], [0, 999], [0, 999], [0, 999])
        mtb = LandActivity("Mountain Biking", [10, 25], [0, 7], [4, 100], [0, 999])
        hiking = LandActivity("Hiking", [6, 26], [0, 5], [5, 999], [0, 80])
        sun_bathing = LandActivity('Beach Day', [22, 40], [0, 4], [6, 999], [0, 50])
        outdoor_climbing = LandActivity('Outdoor Climbing', [15, 28], [0, 4], [6, 999], [0, 90])

        ocean_activity = [sup, surf, body_board, swimming, kite_boarding, wing_surf]
        land_activity = [indoor_climbing, mtb, hiking, sun_bathing, outdoor_climbing]

        with open('ocean_data_input_final', 'r') as f:
            ocean_activity_input = f.read()

        with open('land_data_input_final', 'r') as f:
            land_activity_input = f.read()


        def clean_text_file(text_file):
            lst = []
            a = (text_file[1: -1]).split(',')
            for data in a:
                f_data = float(data.strip())
                lst.append(f_data)
            return lst


        ocean_data_clean_lst = clean_text_file(ocean_activity_input)
        land_data_clean_lst = clean_text_file(land_activity_input)




        for o_activity in ocean_activity:
            o_activity.suitable_sea_day(*ocean_data_clean_lst)

        for l_activity in land_activity:
            l_activity.suitable_land_day(*land_data_clean_lst)

        print('Suitable activities for today are:')
        for activity in days_activity_options:
            print(activity)

Final()