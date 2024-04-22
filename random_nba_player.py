import requests
import random

# Set url to API endpoint for player data
url = 'http://api.balldontlie.io/v1/players'

# Create headers variable including needed API key
headers = {
        'Authorization':'53f7fae1-47e4-4649-8714-ae58eab679bf'
    }

# Create a variable y that will be a random integer between 0 and 600, in 'steps' of 25
y = random.randrange(0,750,25)

# Create a variable response that is an API GET request with the above header, and the cursor
# parameter set to y to give us a 'random' page of 25 players
response = requests.get(url, {'cursor':y}, headers=headers)

# Return the API response as a JSON file
response_data = response.json()

# Create one last variable x that's a random integer between 0 and 24
x = random.randrange(0,25)

# Print out a string that includes a random player's first and last name. This 'random'
# player comes from selecting a random "page" of the data, and within that page of 25
# (since by default pages are 25 items per) select a random player
print(f'{response_data["data"][x]["first_name"]} {response_data["data"][x]["last_name"]} is today\'s random player!')
