"""
Run the code, then it will prompt the user for a team they would like to obtain information about.
It will then print information such as conference standing, wins, and losses.
It scrapes information from https://www.basketball-reference.com.
"""

import requests
from bs4 import BeautifulSoup

# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com"

#Use Beautiful Soup and requests to process information from the url
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

#Declare lists of east and west teams
east_teams = []
west_teams = []

#Get entire table information for east and west teams
east = soup.find(id="confs_standings_E")
west = soup.find(id="confs_standings_W")

#'full_table' contains the team names, as well as seeding, wins, and losses
east_info = east.find_all('tr', class_='full_table')
west_info = west.find_all('tr', class_='full_table')

#Get east team abbrevations
for east_names in east_info:
    east_teams.append(east_names.find('a')['href'][7:10])

#Get west team abbrevations
for west_names in west_info:
    west_teams.append(west_names.find('a')['href'][7:10])

#make a list of wins and losses for each team in the eastern conference
east_wins = [wins.text for wins in east.find_all('td', {'data-stat': 'wins'})]
east_losses = [losses.text for losses in east.find_all('td', {'data-stat': 'losses'})]

#make a list of wins and losses for each team in the western conference
west_wins = [wins.text for wins in west.find_all('td', {'data-stat': 'wins'})]
west_losses = [losses.text for losses in west.find_all('td', {'data-stat': 'losses'})]

#get seeds for team in east conference, splice to remove unwanted characters
#east_seeds = [seeds.text[1:-2] for seeds in east.find_all('span', class_='seed')]
#west_seeds = [seeds.text[1:-2] for seeds in west.find_all('span', class_='seed')]

#list seed numbers, since they don't change
seeds = [i for i in range(1,len(east_teams)+1)]

def get_team_info():
    #Get the team the user would like information for
    team = input("Enter your team's three letter acronym: ").upper()
    try:
        conference = ''
        wins = 0
        losses = 0
        seed = 0

        #If the user inputted team is in the East, search in the east information
        if team in east_teams:
            i1 = east_teams.index(team)
            conference = 'Eastern Conference'
            wins = east_wins[i1]
            losses = east_losses[i1]
            seed = seeds[i1]

        #If the user inputted team is in the West, search in the west information
        else:
            i1 = west_teams.index(team)
            conference = 'Western Conference'
            wins = west_wins[i1]
            losses = west_losses[i1]
            seed = seeds[i1]
        
        #Print desired information about your team:
        print(f'In the {conference}, {team} is currently in the {seed} seed with {wins} wins and {losses} losses.')
    #Notify user that the acronym is not on the list
    except:
        print('The acronym you inputted is not valid, please try again.')

 
get_team_info()