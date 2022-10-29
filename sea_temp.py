class SeaTemp:
    import requests
    import bs4

    headers = {'Accept-Language': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    sea_temp_url = "https://www.seatemperature.org/europe/united-kingdom/bournemouth.htm"
    sea_temp_data = requests.get(url=sea_temp_url, headers=headers)
    sea_soup = bs4.BeautifulSoup(sea_temp_data.text, "html.parser")
    sea_temp_string = sea_soup.find('div', id='sea-temperature')

    sea_temp_c = sea_temp_string.text.strip().split('°C')[0]


print(SeaTemp.sea_temp_c)
