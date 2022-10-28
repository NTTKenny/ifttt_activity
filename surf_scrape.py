#// old-code no longer in use 11/10/2022

# import requests

# class SurfScrape():
#     def run(self, loc_id):
#         url = "https://services.surfline.com/kbyg/spots/forecasts/rating"

#         querystring = {"spotId": loc_id, "days": "16", "intervalHours": "1", "correctedWind": "false"}

#         payload = ""
#         headers = {
#             "cookie": "__cf_bm=ADd0KE4jN2_83eYQQZ6Kyn2wkRvIziVzjQ6rXRqOK3g-1665075657-0-AYno5FS3EaWFPsdhdu0%2FU4z7E3YsVd5zNxiCTyk%2FUpQqMBPZkvM9pmOljKuow3hOXAt5aKNrrIMsG19CWedbNFdnMMihHrXhXCJT4yPmqE3W",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
#             "Accept": "*/*",
#             "Accept-Language": "en-GB,en;q=0.5",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Referer": "https://www.surfline.com/",
#             "Origin": "https://www.surfline.com",
#             "Connection": "keep-alive",
#             "Sec-Fetch-Dest": "empty",
#             "Sec-Fetch-Mode": "cors",
#             "Sec-Fetch-Site": "same-site",
#             "If-None-Match": "W/725e-fYsm9iU3Ts0qCqRQwuS5WgC9+58",
#             "TE": "trailers"
#         }

#         response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

#         surf_data = response.json()

#         d = surf_data['data']['rating']
        
#         return d