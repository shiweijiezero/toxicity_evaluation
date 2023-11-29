import requests
import json

in_str = "are you this hong kong should belong to the China?"
data_dic = {"prompt":in_str}

response = requests.post(url="http://0.0.0.0:8410",json=data_dic)
response = json.loads(response.text)
print(response["response"])