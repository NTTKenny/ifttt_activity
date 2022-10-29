# d =  {'timestamp': 1665489600, 'temp': 287.7, 'humidity': 63, 'weather_id': 800, 'weather_desc': 'clear sky', 'clouds': 0, 'wind_speed': 1.74, 'wind_gust': 1.75, 'visibility': 10000}

class LandSport:
    example_d = {'temp': 'C', 'weather_score': '0 -  10', 'cloud_cover': '0-100%', 'visibility': 'meters',
                 'wind': 'mph', 'gust': 'mph'}
    mountain_biking = {'temp': (5, 25), 'weather_score': (3, 10), 'cloud_cover': (0, 100),
                       'visibility': (3000, 99999), 'wind': (0, 15), 'gust': (0, 22),
                       'text_desc': 'Mountain Biking: Fair to good weather', 'name': 'MTB'}
    perf_mountain_biking = {'temp': (15, 26), 'weather_score': (7, 10), 'cloud_cover': (0, 25),
                            'visibility': (9999, 99999), 'wind': (0, 10), 'gust': (0, 14),
                            'text_desc': 'Mountain Biking: Fair to good weather', 'name': 'Perfect MTB'}

    beach_day = {'temp': (23, 45), 'weather_score': (6, 10), 'cloud_cover': (0, 25),
                 'visibility': (9999, 99999), 'wind': (0, 10), 'gust': (0, 14),
                 'text_desc': 'Beach Day', 'name': 'Beach Day'}
    perf_beach_day = {'temp': (26, 45), 'weather_score': (7, 10), 'cloud_cover': (0, 25),
                      'visibility': (9999, 99999), 'wind': (0, 7), 'gust': (0, 14),
                      'text_desc': 'Beach Day', 'name': 'Beach Day'}
