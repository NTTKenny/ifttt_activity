import json
ow_file = open("surfline_location_raw.json")
ow_data = json.load(ow_file)
count = 0
surfline_locations = []

print(ow_data[0])

for x in ow_data:
    temp_d = {}
    temp_d['lat'] = x['lat']
    temp_d['lon'] = x['lon']
    temp_d['name'] = x['name']
    temp_d['_id'] = x['_id']
    temp_d['timezone'] = x['timezone']
    temp_d['subregionId'] = x['subregionId']
    temp_d['parentTaxonomy'] = x['parentTaxonomy']
    temp_d['abilityLevels'] = x['abilityLevels']
    temp_d['boardTypes'] = x['boardTypes']
    surfline_locations.append(temp_d)

finished_d = {'surf_locations': surfline_locations}

with open('../surf_locations.json', 'w') as f:
    json.dump(surfline_locations, f)