
import requests

def get_weather(zip):
    url = ""

    quarystring = {"zip": zip}

    headers =  {
        "x-rapidapi-key:"""""""
        "x-rapidapi- host"""""""

        }
    response = requests.get(url, headers=headers, params = quarystring)

    return(response.json())

zip = input('enter your zip code:')
print(get_weather(zip))
