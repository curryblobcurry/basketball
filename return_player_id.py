#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:04:17 2024

@author: robcary
"""

def return_player_id(my_player):

    import requests

    url = 'http://api.balldontlie.io/v1/players'

    headers = {
        'Authorization':'53f7fae1-47e4-4649-8714-ae58eab679bf'
        }


    response = requests.get(url, headers=headers)

    response_data = response.json()
    
    my_player = my_player.title()
    # Provide a player name, must have a space between first and last name
    #my_player = 'Brook Lopez'

    # Split the name in two then appropriately name and capture the first and last_name variables.
    if len(my_player.split(' '))!= 2:
        return print('Name is incorrect, need a space between names')
    else:
        first_name = my_player.split(' ')[0]
        last_name = my_player.split(' ')[1]

    # Initialize some loop-related variables
    i = 0
    cursor = 0
    # This loop traverses the "pages" of data returned from the API call, given the 25 items per page.
    # 
    # The loop checks the first name, and if that's a match, then the last name, and if both these match,
    # we print out the player name and their associated ID. We also assign that ID to player_id.
    #
    # I need to figure out how to handle a name that's not in the list of players.
    while i<25:
        if i!=24:
            if response_data["data"][i]["first_name"]==first_name:
                if response_data["data"][i]["last_name"]==last_name:
                    #print(f'{response_data["data"][i]["first_name"]} {response_data["data"][i]["last_name"]}\'s ID is {response_data["data"][i]["id"]}')
                    player_id = response_data["data"][i]["id"]
                    break
            i += 1
        elif i==24:
            if response_data["data"][i]["first_name"]==first_name:
                if response_data["data"][i]["last_name"]==last_name:
                    #print(f'{response_data["data"][i]["first_name"]} {response_data["data"][i]["last_name"]}\'s ID is {response_data["data"][i]["id"]}')
                    player_id = response_data["data"][i]["id"]
                    break
            else:
                    cursor += 25
                    if cursor==750:
                        return print('Couldn\'t find your player :(')
                    response = requests.get(url, {"cursor":cursor}, headers=headers)
                    response_data = response.json()
                    i=0
    return player_id

p_id = return_player_id('robin lopez')
if p_id != None:
    print(f'{p_id}')