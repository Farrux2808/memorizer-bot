import schedule
import time
import telegram
import requests
import datetime

FarruxId = 1571963948
JovidId = 156754695
GroupId = -843964106
bot = telegram.Bot(token="5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag")
def job(depDate, stationFrom, stationTo):
    date = datetime.datetime.now()
    try:
        print('stated:', date)
        Data = {
            "direction": [
                {
                    "depDate": depDate,
                    "fullday": True,
                    "type": "Forward"
                }
            ],
            "stationFrom": stationFrom,
            "stationTo": stationTo,
            "detailNumPlaces": 1,
            "showWithoutPlaces": 0
        }
        headers = {
            'Accept-Language': 'uz',
            # 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiVVNFUiIsImlkIjoiYmZiYzg5MjQtZDEyZi00NjJkLTlmZmYtZTQzMDY3MzE2YzU3Iiwic3ViIjoiOTk4OTM5OTk5MDQ3IiwiaWF0IjoxNjcwNTgxNDMxLCJleHAiOjE2NzA1ODUwMzF9.CUZhTQMjDMPjQuvK_9yVYfwqwIX6OBsEjkObUhNZKlM'
            }
        r = requests.post(url='https://chipta.railway.uz/api/v1/trains/availability/space/between/stations', json=Data, headers=headers)
        tickets = r.json()
        fromPlace = tickets['express']['direction'][0]['passRoute']['from']
        toPlace = tickets['express']['direction'][0]['passRoute']['to']
        for ticket in tickets['express']['direction'][0]['trains'][0]['train']:
            if  ticket['departure']['time'].split(':')[0][0] == '0' and ticket['brand'] == 'Afrosiyob':
                if len(ticket['places']['cars']) > 0:
                    for place in ticket['places']['cars']:
                        if place['indexType'] != '5' or True:
                            bot.send_message(chat_id = GroupId, 
                            text = f"""🎫Bilet: {ticket['brand']} {fromPlace} dan {toPlace} ga
🕔Vaqti: {ticket['departure']['time']} {ticket['departure']['localDate']}
😎Class: {place['typeShow']}""")
    except:
        print('errored:', date)



def runer():
    t = [
        {
            "depDate": "16.04.2023",
            "stationFrom": "2900700",
            "stationTo": "2900000",
        },
        {
            "depDate": "09.04.2023",
            "stationFrom": "2900700",
            "stationTo": "2900000",
        }
    ]
    for i in t:
        job(depDate=i["depDate"], stationFrom=i['stationFrom'], stationTo=i['stationTo'])
        time.sleep(15)
schedule.every(1).minutes.do(runer)

while True:
    schedule.run_pending()
    time.sleep(1)

