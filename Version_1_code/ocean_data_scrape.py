import requests
from bs4 import BeautifulSoup
import json

from openweatherapi import text_day_5


class Ocean_Data_Scrape:
    def __init__(self):
        url = "https://www.metoffice.gov.uk/weather/specialist-forecasts/coast-and-sea/beach-forec" \
              "ast-and-tide-times/gcn8kqhy3#?date=2022-08-04"

        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")


        wave_height = soup.findAll(["span"], class_="height")
        time = soup.findAll(["tr"], class_="step-time")

        wave_height_datapoints = []
        for item in wave_height:
            wave_height_datapoints.append((item['data-value']))


        days = soup.findAll("table", class_='first-day')

        for day in days:
            day0 = (day.find('thead').text.split())


        def time_only_stripper(day_0_scrape):
            lst = []
            reject_lst = [' ', 'Time', '\n']
            for char in day_0_scrape:
              if char in reject_lst:
                continue
              lst.append(char)
            return lst


        day0_len = len(time_only_stripper(day0))

        data_points_days = {0: {'start': 0, 'end': day0_len}, 1: {'start': day0_len, 'end': day0_len+24}, 2: {'start': day0_len+24, 'end': day0_len+33},
                            3: {'start': day0_len+33, 'end': day0_len+41}, 4: {'start': day0_len+41, 'end': day0_len+49}}

        day_lst = text_day_5()


        def data_by_day(data, datapoint_index_d, weekday):
              d = {}
              for number in range(0, 5):
                    d[weekday[number]] = data[datapoint_index_d[number]['start']:datapoint_index_d[number]['end']]
              return d


        finished_data = data_by_day(wave_height_datapoints, data_points_days, day_lst)


        with open('wavedata.json', 'w') as file:
              json.dump(finished_data, file)

Ocean_Data_Scrape()