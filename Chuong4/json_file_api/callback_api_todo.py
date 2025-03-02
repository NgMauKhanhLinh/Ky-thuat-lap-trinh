import json
import requests

api="https://webapi.dantri.com.vn/misc"
response = requests.get(api)
weather=json.loads(response.text)
print(weather)

