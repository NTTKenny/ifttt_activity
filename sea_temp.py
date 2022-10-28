class SeaTemp:
    import requests
    import bs4

    sea_temp_url = "https://www.seatemperature.org/europe/united-kingdom/bournemouth.htm"
    sea_temp_data = requests.get(sea_temp_url)
    sea_soup = bs4.BeautifulSoup(sea_temp_data.text, "html.parser")
    sea_temp_string = sea_soup.find('div', id='sea-temperature')
    
    sea_temp_c = sea_temp_string.text.strip().split('°C')[0]
