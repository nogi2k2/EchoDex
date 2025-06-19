import os
import datetime
from dotenv import load_dotenv
from newsapi import NewsApiClient
import requests
import re
from wolframalpha import Client

load_dotenv(dotenv_path = '..\\Data\\.env')

NEWS = os.getenv('NEWS_API')
WOLFRAMALPHA = os.getenv('WOLFRAMALPHA_API')
WEATHERAPI = os.getenv('OPENWEATHERMAP_API')
TMDB = os.getenv('TMDB_API')
news = NewsApiClient(api_key = NEWS)

def get_ip(_return = False):
    try:
        response = requests.get(f'http://ip-api.com/json/').json()
        if _return:
            return response
        else: 
            return f"Your IP Address is {response['query']}"
    except (requests.exceptions.RequestException, KeyboardInterrupt) as e:
        return None

def get_joke():
    try:
        joke = requests.get('https://v2.jokeapi.dev/joke/Any?format=txt').text
        return joke
    except (KeyboardInterrupt, requests.exceptions.RequestException) as e:
        return None
    
def get_news():
    try:
        top_news = ""
        top_headlines = news.get_top_headlines(language = "en", country = "in")
        for i in range(10):
            top_news += re.sub(r"[|-] [A-Za-z0-9 |:.]*", "", top_headlines["articles"][i]["title"]).replace("’", "'") + "\n"
        return top_news
    except (KeyboardInterrupt, requests.exceptions.RequestException) as e:
        return None

def get_weather(city=''):
    try:
        if not city:
            city = get_ip(True)['city']
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI}&q={city}"
        response = requests.get(url).json()
        if 'error' in response:
            return "Could not fetch weather for the location."
        current = response['current']
        weather = (
            f"It's {current['temp_c']}° Celsius and {current['text']}\n"
            f"But feels like {current['feelslike_c']}° Celsius\n"
            f"Wind is blowing at {current['wind_kph']} km/h\n"
            f"Visibility is {current['vis_km']} km"
        )
        return weather
    except (KeyboardInterrupt, requests.exceptions.RequestException):
        return None

def get_popular_movies():
    try:
        response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB}&region=IN&sort_by=popularity.desc&"
                                f"primary_release_year={datetime.date.today().year}").json()
    except requests.exceptions.RequestException:
        return None
    
    try:
        print()
        for movie in response["results"]:
            title = movie["title"]
            print(title)
    except KeyError:
        return None

def get_popular_tvseries():
    try:
        response = requests.get(f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB}&region=IN&sort_by=popularity.desc&"
                                f"primary_release_year={datetime.date.today().year}").json()
    except requests.exceptions.RequestExeption:
        return None

    try:
        print()
        for series in response["results"]:
            title = series["name"]
            print(title)
    except KeyError:
        return None