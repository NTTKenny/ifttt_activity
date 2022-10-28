import json
import bs4
import requests

header = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}


def surf_height_report(url, name):
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    table = soup.findAll("div", class_="quiver-spot-forecast-summary__wrapper")
    surf = table[0].find("span", class_="quiver-surf-height")
    surf_clean = surf.text.replace('FT', '').replace('+', '').replace('Flat', '0').split('-')
    d = {name: [surf_clean[-1], surf_clean[0]]}
    return d


def surf_quality_report(url, name):
    data = requests.get(url, headers=header)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    desc = soup.findAll('div', class_='quiver-spot-report')
    desc_string = (desc[0].text).split("Surf height")
    text_surf_quality = desc_string[0].lower()
    rating_scale = {'flat': 1, 'very poor': 2, 'poor': 3, 'poor to fair': 4, 'fair': 5, 'fair to good': 6,
                    'good': 7, 'very good': 8, 'good to epic': 9, 'epic': 10, 'report coming soon': 0}
    surf_rating_10 = rating_scale[text_surf_quality]
    return {name: surf_rating_10}


surf_spots_urls ={"Bournemouth": "https://www.surfline.com/surf-report/bournemouth/584204214e65fad6a7709cf4?camId=5834968e3421b20545c4b525", "Highcliffe": "https://www.surfline.com/surf-report/highcliffe/604a75d1d397152373ccb0d8", "Kimmeridge Bay": "https://www.surfline.com/surf-report/kimmeridge-bay/5842041f4e65fad6a7708e1f"}


surf_quality_lst = []
surf_height_lst = []

for key, value in surf_spots_urls.items():
    surf_quality_lst.append(surf_quality_report(value, key))
    surf_height_lst.append(surf_height_report(value, key))

# print(surf_quality_lst)
# print(surf_height_lst)

with open('surf_quality.json', 'w') as f:
    json.dump(surf_quality_lst, f)

with open('surf_height.json', 'w') as f:
    json.dump(surf_height_lst, f)





sea_temp_url = "https://www.seatemperature.org/europe/united-kingdom/bournemouth.htm"

sea_temp_data = requests.get(sea_temp_url)
sea_soup = bs4.BeautifulSoup(sea_temp_data.text, "html.parser")
sea_temp_string = sea_soup.find('div', id='sea-temperature')
sea_temp_c = sea_temp_string.text.strip().split('°C')[0]


with open('seatemp_cels.txt', 'w') as f:
    f.write(sea_temp_c)
