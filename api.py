# import requests
#
# api_url = "http://numbersapi.com/"
#
# params = {
#     'json': 'true'
# }
#
# with open("dataset_24476_3.txt") as f:
#     numbers = f.readlines()
# for number in numbers:
#     res = requests.get(api_url + str(number.strip()) + "/math", params=params)
#     date = res.json()
#     if date["found"] == True:
#         print("Interesting")
#     else:
#         print("Boring")

import requests
import json

token_url = "https://api.artsy.net/api/tokens/xapp_token"
client_Id = "caae130d3b10af40e6e0"
client_Secret = "74e8b0f42df3fa8d3ae6f2dfc273acc8"

res = requests.post(token_url,
                    data={
                        "client_id": client_Id,
                        "client_secret": client_Secret
                    })
j = json.loads(res.text)
token = j["token"]

headers = {"X-Xapp-Token": token}
data = {}
api_url = "https://api.artsy.net/api/artists/"
with open("dataset_24476_4.txt") as f:
    ids= f.readlines()
for id in ids:
    res = requests.get(api_url +id.strip(), headers=headers)
    j = json.loads(res.text)
    data[j["birthday"]]= j["sortable_name"]
for x in sorted(data.keys()):
    print(data[x])

