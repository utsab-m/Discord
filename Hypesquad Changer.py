import requests
import os
import random

token = "ENTER TOKEN HERE"

def hypesquad():
    os.system('title Hypesquad Changer')
    os.system('cls')
    request = requests.Session()
    headers = {
      'authorization': token,
      'content-type': 'application/json',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }    
    house = input('Choices are: bravery, brilliance, balance, random, or leave\nEnter the house you would like: ')
    if house == "bravery":
        payload = {'house_id': 1}
        txt = "Trying to give hypesquad bravery"
        success = "Successfully gave hypesquad bravery"
        do = request.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload, timeout=10)
    elif house == "brilliance":
        payload = {'house_id': 2}
        txt = "Trying to give hypesquad brilliance"
        success = "Successfully gave hypesquad brilliance"
        do = request.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload, timeout=10)
    elif house == "balance":
        payload = {'house_id': 3}
        txt = "Trying to give hypesquad balance"
        success = "Successfully gave hypesquad balance"
        do = request.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload, timeout=10)
    elif house == "random":
        houses = [1, 2, 3]
        randomhouse = random.choice(houses)
        payload = {'house_id': randomhouse}
        txt = "Trying to give a random hypesquad"
        success = "Successfully gave a random hypesquad"
        do = request.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload, timeout=10)
    elif house == "leave":
        txt = "Leaving hypesquad"
        success = "Left hypesquad"
        do = request.delete('https://discord.com/api/v9/hypesquad/online', headers=headers)
    try:
        print(txt)
        os.system('timeout -t 3 >nul')
        print(do)
        if do.status_code == 204 or do.status_code == 200:
            print(success)
        else:
            print("Failed to give hypesquad")
        os.system('pause')
    except Exception as e:
        print('Enter either bravery, brilliance, balance, or random.')
        os.system('pause')
        os.system('title Invalid Hypesquad')
        os.system('cls')

while True:
    hypesquad()