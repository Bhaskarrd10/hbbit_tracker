import requests

USER_NAME = "Bhaskarrd"
TOKEN = "hsfkfhasdkfhkfhskfjh"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "user_name": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.put(url=pixela_endpoint, json=user_params)



graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": ""
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)

print(response.text)