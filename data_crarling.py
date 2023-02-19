import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://understat.com/league/EPL/2018"

# Send an HTTP request to the website and get the HTML response
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that contains the player data and extract each row
table = soup.find_all("table")[0]
rows = table.find_all("tr")[1:]

# Define a dictionary to store the player data
players_data = {}

# Iterate through each row and extract the player data
for row in rows:
    # Extract the player name
    player_name = row.find("a").get_text()

    # Extract the player goals, assists, xG, and xA data
    data = row.find_all("td")[5:9] + row.find_all("td")[10:11]
    player_data = [d.get_text() for d in data]

    # Add the player data to the dictionary
    players_data[player_name] = player_data

# Print the player data
for player, data in players_data.items():
    print(player, data)
