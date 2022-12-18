
import datetime
from playsound import playsound


time = input("Enter hour (24 hour format):")


while True:
    time_Ac = datetime.datetime.now()
    now  = time_Ac.strftime("%H:%M:%S")
    if now == time:
        playsound('Arabic_Remix_-_Fi_Ha__28_Burak_Balkan_Remix__29__23ArabicVocalMix (1).mp3')
    elif now> time:
        break

