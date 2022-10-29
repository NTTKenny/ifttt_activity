import requests
import json
from cmath import inf
from math import sqrt as root


class PostCode:
    surf_loc_file = open('surf_locations.json')
    surf_loc_data = json.load(surf_loc_file)

    def postcode_to_coord(self, post_code):
        post_code = 'bh13 7jh'
        url = "https://api.postcodes.io/postcodes/{postcode}".format(
            postcode=post_code)
        response = requests.get(url).json()['result']

        postcode_coords = {
            'lon': response['longitude'], 'lat': response['latitude']}

        return postcode_coords

    def closest_beach(self, user_coordinate_dict, surf_locations: list):
        user_lon, user_lat = user_coordinate_dict['lon'], user_coordinate_dict['lat']
        closest_beach = None
        distance_from_coords = float(inf)

        for location_dict in surf_locations:
            surf_lon, surf_lat = location_dict['lon'], location_dict['lat']
            distance = root((user_lon - surf_lon)**2 +
                            (user_lat - surf_lat)**2)
            if distance < distance_from_coords:
                closest_beach = location_dict
                distance_from_coords = distance

        return closest_beach
