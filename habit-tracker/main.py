# main.py

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "YOUR_PIXELA_USERNAME"      # change to your Pixela username
PASSWORD = "YOUR_PIXELA_TOKEN"         # change to your Pixela token
graph_id = "graph2"                    # ID of the graph you want to use

user_params = {
    "token": PASSWORD,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment these two lines the very first time to create your Pixela user,
# response = requests.post(url=pixela_endpoint, json=user_params)
# then comment them again so they don't run every time.
# print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Trading Journal",
    "unit": "USD",
    "type": "float",
    "color": "ajisai", #Means purple
}

headers = {
    "X-USER-TOKEN": PASSWORD,
}

# Uncomment these two lines once to create the graph,
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# then comment them out afterwards.
# print(response.text)

# --------------------
# ADD TODAY'S VALUE
# --------------------
today = datetime.now()
post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("What is the PNL for today? "),
}

print(today.strftime("%Y%m%d"))

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
graph_response = requests.post(
    url=post_pixel_endpoint,
    headers=headers,
    json=post_pixel_params,
)
print(graph_response.text)

# --------------------
# OPTIONAL: UPDATE / DELETE A SPECIFIC DAY
# --------------------
# To update or delete a specific date, change the date in the URL below,
# then uncomment the request you want to use.

update_pixel_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/20251223"
)

update_pixel = {
    "quantity": "0",
}

# UPDATE example:
# pixel_response = requests.put(url=update_pixel_endpoint,headers=headers,json=update_pixel,)
# print(pixel_response.text)

# DELETE example:
# pixel_response = requests.delete(url=update_pixel_endpoint,headers=headers,)
# print(pixel_response.status_code)
