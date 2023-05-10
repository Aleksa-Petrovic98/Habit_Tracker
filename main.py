# Import the requests module to make HTTP requests
import requests

# Import the datetime module to work with dates and times
from datetime import datetime

from authentication import authentication

TOKEN = authentication.Auth.TOKEN
USERNAME = authentication.Auth.USERNAME


# Set the base URL for the Pixela API
pixela_endpoint = "https://pixe.la/v1/users"

# Set the ID for the graph to be created
GRAPH_ID = 'graph1'

# Set the parameters required to create a new user on Pixela
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Send a POST request to the Pixela API to create a new user
# Commenting out the following two lines so it doesn't create a new user each time the code runs
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# Set the endpoint for creating a new graph on Pixela
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# Set the configuration for the graph to be created
graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

# Set the headers required for authentication with the Pixela API
headers = {
    'X-USER-TOKEN': TOKEN
}

# Send a POST request to the Pixela API to create a new graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Print the response from the API to the console
print(response.json())

# Set the endpoint for creating a new pixel on the graph
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

# Set the data for the new pixel to be created
today = datetime.now()
pixel_data = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '25',
}

# Send a POST request to the Pixela API to create a new pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# Print the response from the API to the console
print(response.json())

# Set the endpoint for updating the value of a pixel on the graph
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# Set the new value for the pixel
new_pixel_data = {
    'quantity': '4.5'
}

# Send a PUT request to the Pixela API to update the value of the pixel
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# Print the response from the API to the console
print(response.json())

# Set the endpoint for deleting a pixel from the graph
delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# Send a DELETE request to the Pixela API to delete the pixel
response = requests.delete(url=delete_endpoint, headers=headers)

# Print the response from the API to the console
print(response)
