import requests


class WaveScrape:
    def wave_run(self, surfline_location_id):
        url = "https://services.surfline.com/kbyg/spots/forecasts/wave"

        querystring = {"spotId": surfline_location_id,
                       "days": "16", "intervalHours": "1", "": ""}

        payload = ""
        headers = {
            "cookie": "__cf_bm=SwKL5hQhFMY7UBCuRH_.v9Apw__QqJo7NOKN0.v1FJQ-1665056020-0-Ac6kr1E%2FY43TXzqPa2lCv%2F5Az17JGSXYyoPWeDeIwODw1iYSyr9I5ZVnrdrWtKbkjNN5VNvoXgDsX3SbDSH%2ByBp9yy0hrG1b1j9AjtVx51H4",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "*/*",
            "Accept-Language": "en-GB,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.surfline.com/",
            "Origin": "https://www.surfline.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "If-None-Match": "W/3cff9-quHq/Dh7zs4GUnfKOyyZU7IYlOs",
            "TE": "trailers"
        }

        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)

        data = response.json()

        wave_info = data['data']['wave']

        d = {}

        for dic in wave_info:
            time = dic['timestamp']
            d[time] = dic

        return d

    def surf_run(self, surfline_location_id):
        url = "https://services.surfline.com/kbyg/spots/forecasts/rating"

        querystring = {"spotId": surfline_location_id, "days": "16", "intervalHours": "1",
                       "correctedWind": "false"}

        payload = ""
        headers = {
            "cookie": "__cf_bm=ADd0KE4jN2_83eYQQZ6Kyn2wkRvIziVzjQ6rXRqOK3g-1665075657-0-AYno5FS3EaWFPsdhdu0%2FU4z7E3YsVd5zNxiCTyk%2FUpQqMBPZkvM9pmOljKuow3hOXAt5aKNrrIMsG19CWedbNFdnMMihHrXhXCJT4yPmqE3W",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "*/*",
            "Accept-Language": "en-GB,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.surfline.com/",
            "Origin": "https://www.surfline.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "If-None-Match": "W/725e-fYsm9iU3Ts0qCqRQwuS5WgC9+58",
            "TE": "trailers"
        }

        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)
        surf_data = response.json()
        lst = surf_data['data']['rating']

        return lst

    def wind_run(self, surfline_location_id):

        url = "https://services.surfline.com/kbyg/spots/forecasts/wind"

        querystring = {"spotId": surfline_location_id,
                       "days": "16", "intervalHours": "1", "corrected": "false"}

        payload = ""
        headers = {
            "cookie": "__cf_bm=iJDv8VVbXPO6mOKrtCKp5tFTlSC_vWFJUlmyGBwXx2A-1665079314-0-AaDvA0K3iefh4Fne9W9u66VnQoRwwmpps7nSX60tTYpHn%2Ff8x%2FEoeWOhUFauoik2T8n5g3mWg9AupAvCEwLbxvgg1b7o5xK%2FsrufZ5nfaqQZ",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "*/*",
            "Accept-Language": "en-GB,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.surfline.com/",
            "Origin": "https://www.surfline.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "If-None-Match": "W/ceef-auT7PMhjZ04PNDOmRk/j5x6w/X0",
            "TE": "trailers"
        }

        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)

        lst = response.json()['data']['wind']

        return lst


class OceanWeather():
    ws = WaveScrape()

    def beach_wind_to_value(wind_direction_str):
        score = None
        if wind_direction_str == 'Offshore':
            score = 0
        elif wind_direction_str == 'Cross-shore':
            score = 1
        elif wind_direction_str == 'Onshore':
            score = 2
        return score

    def run(self, surfline_id):
        wave_data = self.ws.wave_run(surfline_id)
        wave_data_times = wave_data.keys()
        surf_quality_lst = self.ws.surf_run(surfline_id)
        wind_lst = self.ws.wind_run(surfline_id)

        for key in wave_data:
            swell_lst = wave_data[key]['swells']
            wave_data[key]['swells'] = swell_lst[0]  # first swell only
            wave_data[key]['raw_height_average'] = (
                wave_data[key]['surf']['raw']['min'] + wave_data[key]['surf']['raw']['max']) / 2
            wave_data[key]['surf_min'] = wave_data[key]['surf']['min']
            wave_data[key]['surf_max'] = wave_data[key]['surf']['max']
            del wave_data[key]['surf']

        for surf_rating_dict in surf_quality_lst:
            key = surf_rating_dict['timestamp']
            rating1 = surf_rating_dict['rating']['key']
            rating2 = surf_rating_dict['rating']['value']
            wave_data[key]['rating_text'] = rating1
            wave_data[key]['rating_value'] = rating2

        for wind_dict in wind_lst:
            key = wind_dict['timestamp']
            if key in wave_data_times:
                wave_data[key]['wind_speed'] = wind_dict['speed']
                wave_data[key]['wind_direction'] = wind_dict['direction']
                wave_data[key]['directionType'] = OceanWeather.beach_wind_to_value(
                    wind_dict['directionType'])
                wave_data[key]['windGust'] = wind_dict['gust']

        return wave_data
