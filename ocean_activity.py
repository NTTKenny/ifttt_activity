class OceanSport:
    # Temperature (°C): 'temp', Weather rating (0-10), greater = more desireable: 'weather_score', Visibility (M): 'visibility', Cloud cover (percentage): 'cloud_cover'
    # Surf maximum height (Ft): 'surf_max', Surf mimimun height (Ft): 'surf_min', Wind gust (Mph): 'windGust', Wind speed (Mph): 'wind_speed', Surf wave quality (0-5), '2 = poor to fair': 'rating_value'
    # Wind direction in relation to beach (0-2), 0 = Offshore, 1 = Cross-shore, 2 = Onshore: 'directionType', Minmum sea temperature (°C) - Note: single value not range: 'sea_temp_min',
    # Activity name (string): 'name'. Description of weather (string): 'desc'

    surfing = {'temp': (12, 45), 'weather_score': (4, 11), 'visibility': (5000, 99999), 'cloud_cover': (0, 100), 'surf_max': (3, 8), 'surf_min': (2, 5), 'windGust': (
        0, 22), 'wind_speed': (0, 16), 'rating_value': (2, 10), 'directionType': (1, 2), 'sea_temp_min': 10.1, 'name': 'Surfing', 'desc': 'Good conditions for surfing'}
    paddle_boarding = {'temp': (20, 45), 'weather_score': (7, 11), 'visibility': (5000, 99999), 'cloud_cover': (0, 50), 'surf_max': (0, 1), 'surf_min': (0, 0), 'windGust': (
        0, 12), 'wind_speed': (0, 7), 'rating_value': (0, 10), 'directionType': (1, 2), 'sea_temp_min': 15.0, 'name': 'SUP', 'desc': 'Good conditions for Paddleboarding'}
    # beginner_surfing = ' '
    body_boarding = {'temp': (12, 45), 'weather_score': (4, 11), 'visibility': (5000, 99999), 'cloud_cover': (0, 100), 'surf_max': (3, 10), 'surf_min': (3, 6), 'windGust': (
        0, 22), 'wind_speed': (0, 16), 'rating_value': (1, 10), 'directionType': (1, 2), 'sea_temp_min': 10.1, 'name': 'Surfing', 'desc': 'Good conditions for surfing'}
    perf_paddle_boarding = {'temp': (25, 45), 'weather_score': (8, 11), 'visibility': (5000, 99999), 'cloud_cover': (0, 20), 'surf_max': (0, 0), 'surf_min': (0, 0), 'windGust': (
        0, 12), 'wind_speed': (0, 5), 'rating_value': (0, 10), 'directionType': (1, 2), 'sea_temp_min': 15.0, 'name': 'Perfect SUP', 'desc': 'Good conditions for Paddleboarding'}
    kayaking = {'temp': (18, 45), 'weather_score': (7, 11), 'visibility': (5000, 99999), 'cloud_cover': (0, 50), 'surf_max': (0, 1), 'surf_min': (0, 0), 'windGust': (
        0, 12), 'wind_speed': (0, 7), 'rating_value': (0, 10), 'directionType': (1, 2), 'sea_temp_min': 12.0, 'name': 'Kayaking', 'desc': 'Good conditions for sea kayaking'}
    wild_sea_swimming = {'temp': (16, 45), 'weather_score': (6, 11), 'visibility': (5000, 99999), 'cloud_cover': (0, 100), 'surf_max': (0, 2), 'surf_min': (0, 0), 'windGust': (
        0, 12), 'wind_speed': (0, 7), 'rating_value': (0, 10), 'directionType': (1, 2), 'sea_temp_min': 12.0, 'name': 'Sea Swimming', 'desc': 'Good conditions for swimming'}
    keys = ['temp', 'weather_score', 'visibility', 'cloud_cover', 'surf_max', 'surf_min',
            'windGust', 'wind_speed', 'rating_value', 'directionType', 'sea_temp_min', 'name', 'desc']
