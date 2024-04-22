#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:45:04 2024

@author: robcary
"""

# This function takes an NBA team and populates a list with player IDs for that team.
def get_nba_team_player_ids(team):
    import requests

    url = 'http://api.balldontlie.io/v1/players'

    headers = {
        'Authorization':'53f7fae1-47e4-4649-8714-ae58eab679bf'
        }

    response = requests.get(url, headers=headers)

    response_data = response.json()

    i = 0
    cursor = 0
    team_roster = []
    while i<25:
        if i!=24:
            if response_data["data"][i]["team"]["full_name"]==team:
                if len(team_roster)>2:
                    if (response_data["data"][i]["id"]==team_roster[-1]):
                        break
                    team_roster.append(str(response_data["data"][i]["id"]))
                    #print(f'{team_roster} ')
                else:
                    team_roster.append(str(response_data["data"][i]["id"]))
                    #print(f'{team_roster} ')
            i += 1
        elif i==24:
            if response_data["data"][i]["team"]["full_name"]==team:
                if len(team_roster)>2:
                    if (response_data["data"][i]["id"]==team_roster[-1]):
                        break
                else:
                    team_roster.append(str(response_data["data"][i]["id"]))
                    #print(f'{team_roster} ')
        #else:
            cursor += 25
            if cursor==750:
                break
            response = requests.get(url, {"cursor":cursor}, headers=headers)
            response_data = response.json()
            i = 0
    return team_roster

get_nba_team_player_ids('Milwaukee Bucks')
