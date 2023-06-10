import requests
from bs4 import BeautifulSoup
import json


# https://github.com/Haj4li 


cityName = "Mashhad"

def getWeather(cityName):
    url = 'https://www.eldoradoweather.com/forecast/iran/{}.php'.format(cityName)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []
    days = soup.select('td td div:nth-child(1)')
    statues = soup.select('td td div:nth-child(3) span')
    nighttemp = soup.select('.leftside div span~ span+ span')
    daytemp = soup.select('td td td div:nth-child(5) > span:nth-child(1) , td td td div:nth-child(5) > span:nth-child(1) , td td div:nth-child(4) > span:nth-child(1)')
    cp = soup.select('div:nth-child(6) span:nth-child(1)')

    counter = 0
    ccounter = 0
    for day in days:
        day = day.text.replace(" ", "").replace("\n", "")
        if (len(day) < 2):
            continue
        
        cstatues = statues[ccounter].text.replace(" ", "").replace("\n", "")
        nightc = nighttemp[counter].text.split(' ')[0]
        nightf = nighttemp[counter+1].text.split(' ')[0]

        dayc = daytemp[counter].text.split(' ')[0]
        dayf = daytemp[counter+1].text.split(' ')[0]
        cpp = cp[ccounter].text.replace(" ", "").replace("\n", "")

        dset = {
            "date" : day,
            "Statues": cstatues,
            "Night": {
                "C" : nightc,
                "F" : nightf,
            },
            "Day": {
                "C" : dayc,
                "F" : dayf,
            },
            "ChanceOfPrecipitation": cpp
        }
        data.append(dset)

        counter += 2
        ccounter += 1

    return(data)

data = getWeather(cityName)

with open('data.json', 'w') as file:
    json.dump(data, file)

print("Data Saved .")