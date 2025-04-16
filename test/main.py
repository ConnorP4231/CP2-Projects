import requests

def get_location(ip_address=''):
    # Leave ip_address blank to get your own location
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    
    if response.status_code == 200:
        data = response.json()
        IP = data.get('ip')
        City = data.get('city')
        Region = data.get('region')
        Country = data.get('country')
        LatLong = data.get('loc')

        print(f'How does it feel living in {City}, {Region}, {Country}. Your IP address is {IP} and your latitude and longitude is {LatLong}.')
    else:
        print("Failed to retrieve location")

get_location()  # gets your own location
# get_location("8.8.8.8")  # gets Google's public DNS location


import os

# Get the current logged-in user
name = os.getlogin()

formatted_name = name.replace('.', ' ').split()
formatted_name[0] = formatted_name[0].capitalize()

# Join the parts back together
formatted_name = ' '.join(formatted_name)

print(formatted_name)

