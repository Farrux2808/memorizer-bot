import schedule
import time
import telegram
import requests
import datetime

bot = telegram.Bot(token="5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag")
def job():
    date = datetime.datetime.now()
    try:
        print('stated:', date)
        Data = {
            "direction": [
                {
                    "depDate": "24.02.2023",
                    "fullday": True,
                    "type": "Forward"
                }
            ],
            "stationFrom": "2900000",
            "stationTo": "2900700",
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
            if (ticket['brand'] == 'Sharq' or ticket['brand'] == 'Afrosiyob') and (ticket['departure']['time'].split(':')[0] == '19'):
                if len(ticket['places']['cars']) > 0:
                    for place in ticket['places']['cars']:
                        if place['indexType'] != '5':
                            bot.send_message(chat_id = 1571963948, 
                            text = f"""🎫Bilet: {ticket['brand']} {fromPlace} dan {toPlace} ga
🕔Vaqti: {ticket['departure']['time']} {ticket['departure']['localDate']}
😎Class: {place['typeShow']}""")
    except:
        print('errored:', date)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

