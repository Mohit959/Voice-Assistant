import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
import time
import requests
import json
import wolframalpha
import wikipedia
import datetime
from googletrans import Translator
import urllib.request as url
import re
import smtplib as smtp
import pywhatkit as kit
import numberguess
import password

# import yfinance

crypto_api='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=usd'
wolfram_api='6V9L46-T73W33J9JV'
chuck_norris_api="https://api.chucknorris.io/jokes/random"
new_api_key="e03e4c1d4b2040bab673e23c7b243260"
weather_api_key="9963e71b6a74489296855a0919a0d61f"
distance_api_key="FFB17vGsug4JmyeDDDlwPfqGDiHe4ZL5"


def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source);
        text="";
         
        try:
            text=r.recognize_google(audio)
        
        except sr.RequestError as re:
            print(re)

        except sr.UnknownValueError as uve:
            print(uve)

        except sr.WaitTimeoutError as wte:
            print(wte)

    text=text.lower()
    return text;


def talk(text):
    file_ka_naam="audio.mp3"
    voice=gTTS(text=text,lang="en",slow=False)
    voice.save(file_ka_naam)
    #time.sleep(1)
    playsound(file_ka_naam)
    os.remove(file_ka_naam)

def talkInDestLang(text,lang):
    file_ka_naam="audio.mp3"
    voice=gTTS(text=text,lang=lang,slow=False)
    voice.save(file_ka_naam)
    #time.sleep(1)
    playsound(file_ka_naam)
    os.remove(file_ka_naam)

#talk("main hemant hu or main apne project par kaam kar raha hu")

def reply(text):

    #smallTalk
    if 'what' in text and 'name' in text:
        talk("Hi I am Reema I am your Voice Assistant")

    #smallTalk
    elif 'goodbye' in text or 'bye' in text:
        talk("mujhe bhi baat karke maza aaya")

    #smallTalk
    elif 'when' in text and 'sleep' in text:
        talk("i don't sleep ,I am available 24 into 7")

    #smallTalk
    elif 'favourite' in text and 'song' in text:
        talk("my favourite song is Rowdy Baby")

    #smallTalk
    elif 'you' in text and 'stupid' in text:
        talk("No I am not stupid")
    
    #cryptoCurrency - Bitcoin
    elif 'bitcoin' in text:
        response=requests.get(crypto_api)
        crypto_json=response.json()
        talk("Current price of bitcoin is" + str(crypto_json['bitcoin']['usd'])+" US Dollar")

    #cryptoCurrency - Dogecoin
    elif 'dogecoin' in text:
        response=requests.get(crypto_api)
        crypto_json=response.json()
        talk("Current price of Dogecoin is" + str(crypto_json['dogecoin']['usd'])+" US Dollar")

    #cryptoCurrency - Ethereum
    elif 'ethereum' in text:
        response=requests.get(crypto_api)
        crypto_json=response.json()
        talk("Current price of ethereum is" + str(crypto_json['ethereum']['usd'])+" US Dollar")

    # Basic Questions
    elif 'prime minister' in text or 'president' in text or 'capital' in text or 'date of birth'in text or 'ceo' in text or 'wife' in text or 'husband' in text or 'city' in text or 'country' in text :
        walfram_alpha(text)

    # Calculator
    elif '+' in text or '-' in text or 'multiply' in text or '*' in text or '/' in text or 'root' in text:
        walfram_alpha_calculator(text)

    #translation of languages
    elif 'translate' in text:
        while True:
            talk("What do you need to translate?")
            text=listen()
            if text!='turn off translator' and text!=' ':
                translate(text)
            else:
                talk("Translator is turned off,what else you want to do")
                break

    # this is for jokes
    elif 'chuck norris' in text:
        chuck_norris()

    # To get some news headlines
    elif 'news' in text:
        talk("let me tell you some headlines");
        get_news()
    
    #To get weather
    elif 'weather' in text:
        get_weather()

    #To calculate distance between two cities
    elif 'distance' in text:
        get_distance()

    # To search something on wikipedia
    elif 'wikipedia' in text:
        wikipedia_info()

    elif 'time' in text:
        time_now()

    elif 'week' in text or 'day'in text:
        weekday_now()

    elif 'youtube' in text or 'tube' in text:
        playVideo()

    elif 'game' in  text:
        numberguess.game();
    elif "generate password" in text:
        generatepassword.function()
    elif "password manager" in text:
        password.passwordmanager()

    else:
        talk("I am not getting What you are speaking?")

def execute():
    talk("hi i am Reema ,What's your name?");
    name=listen()
    talk(name + "How are you?");
    while True:
        message=listen()
        print(message)
        reply(message)

        if 'goodbye' in message:
            break;

def walfram_alpha(text):
    client =wolframalpha.Client(wolfram_api)
    res = client.query(text)
    ans=next(res.results).text
    print(ans)
    talk(ans);


def walfram_alpha_calculator(text):
    client =wolframalpha.Client(wolfram_api)
    res = client.query(text)
    ans=next(res.results).text
    print(ans)
    talk(ans);

def translate(text):
    translator=Translator()
    out=translator.translate(text,dest="de").text
    talkInDestLang(out,"de")

def chuck_norris():
    data=requests.get(chuck_norris_api);
    json=data.json()
    joke=json['value'];
    print(joke)
    talk(joke)

def get_news():
    news_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=" +new_api_key
    data=requests.get(news_url).json()
    articles = data['articles']
    news_headlines=[]
    for art in articles:
        headlines=art['title']
        news_headlines.append(headlines)
    for i in range(3):
        print(news_headlines[i])
        talk(news_headlines[i])

def get_weather():
    talk("what city are u interested in?")
    city=listen()
    print(city)
    weather_api_url="https://api.weatherbit.io/v2.0/current?&city="+ city + "&key=" + weather_api_key
    data=requests.get(weather_api_url)
    json=data.json()
    temp=json['data'][0]['temp']
    weather=json['data'][0]['weather']['description']
    final_weather="Temperature in "+city+" is "+str(temp) +" degrees and you can see "+weather
    print(final_weather)
    talk(final_weather)

def get_distance():
    talk("let me know the starting point")
    location_one=listen()
    time.sleep(1)
    talk("ending point")
    location_two=listen()
    print(location_one)
    print(location_two)
    distance_api_url="https://www.mapquestapi.com/directions/v2/route?key=FFB17vGsug4JmyeDDDlwPfqGDiHe4ZL5&from=" +location_one + "&to="+ location_two+"&unit=k"
    data=requests.get(distance_api_url)
    json=data.json()
    dist=json['route']['distance']
    res="The distance between "+location_one+" and "+location_two+" is "+str(dist) +" kilometres"
    print(res)
    talk(res)


def wikipedia_info():
    talk("Let me know What i can search for u on wikipedia")
    input=listen()
    res=wikipedia.summary(input,sentences=1)
    print(res)
    talk(res)

def time_now():
    x=datetime.datetime.now()
    hour=x.strftime("%I")
    min=x.strftime("%M")
    meridian=x.strftime("%p")
    time="Current time is "+hour+":"+min+" "+meridian
    print(time)
    talk(time)

def weekday_now():
    x=datetime.datetime.now()
    weekday=x.strftime("%A")
    print(weekday)
    talk(weekday)

def playVideo():
    talk("What do you want to play")
    text=listen()
    search_keyword=text
    html = url.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    # used to find first video of youtube page
    link= re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(link);  #link of youtube video
    kit.playonyt(link);

def sendMail():
    s = smtp.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("", "")
    # message to be sent
    message = "How are you?"
    # sending the mail
    s.sendmail("", "", message)
    # terminating the session
    s.quit()

execute()

# email           david
# google
# ytube           done
# call            
# change voice    done
# games           mohit done
# alarm 

#password manager & generatorn
# numberguess.game()















