import json
import requests

url = "https://services.surfline.com/kbyg/mapview"

querystring = {"south":"41.50857729743935","west":"-57.65625000000001","north":"58.35563036280967","east":"51.32812500000001"}

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
    "TE": "trailers"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

response_dict = response.json()

spots = response_dict['data']['spots']

with open('surfline_location_raw.json', 'w') as f:
    json.dump(spots, f)
print(spots)