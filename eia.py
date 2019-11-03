import requests
import json
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDZ4CKmUWDamVjSONXT4zEV6Rhj0roFdDU')




def jsonp(response):
    text = json.dumps(response, sort_keys=True, indent=4)
    print(text)

# eia_response = requests.get("http://api.eia.gov/series/?")


eia_response = requests.get("http://api.eia.gov/series/?api_key=227d6b5a4d4bb06fe01a8cff08b9a49e&series_id=ELEC.CONS_TOT.COW-AL-99.A")

unprocessed_data = jsonp(eia_response.json())

# response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
#
# print(response.status_code)
