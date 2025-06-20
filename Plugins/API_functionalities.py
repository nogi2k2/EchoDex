import os
import datetime
from dotenv import load_dotenv
from newsapi import NewsApiClient
import requests
import re
from wolframalpha import Client

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, 'Data', '.env')
load_dotenv(dotenv_path=ENV_PATH)

NEWS = os.getenv('NEWS_API')
WOLFRAMALPHA = os.getenv('WOLFRAMALPHA_API')
WEATHERAPI = os.getenv('WEATHER_API')
TMDB = os.getenv('TMDB_API')

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
        api_key = NEWS
        url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=10&apiKey={api_key}"

        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            print("NewsAPI Error:", data.get("message", "Unknown error"))
            return "Could not fetch news."

        top_news = ""
        for article in data["articles"]:
            title = article.get("title", "No Title")
            title = re.sub(r"[|-] [A-Za-z0-9 |:.]*", "", title).replace("’", "'")
            top_news += f"- {title}\n"

        return top_news or "No news found."

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return "Network error."
    except Exception as e:
        print("Error in get_news():", e)
        return "An error occurred while fetching news."
    
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
            f"It's {current['temp_c']}° Celsius and {current['condition']['text']}\n"
            f"But feels like {current['feelslike_c']}° Celsius\n"
            f"Wind is blowing at {current['wind_kph']} km/h\n"
            f"Visibility is {current['vis_km']} km"
        )
        return weather
    except (KeyboardInterrupt, requests.exceptions.RequestException):
        return None
    
def get_general_response(query):
    client = Client(app_id=WOLFRAMALPHA)
    try:
        response = client.query(query)
        return next(response.results).text
    except (StopIteration, AttributeError) as e:
        return None
    except KeyboardInterrupt:
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
        url = f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB}&region=IN&sort_by=popularity.desc"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("Fetched data successfully")

        for series in data.get("results", []):
            title = series.get("name", "Unknown")
            print(title)

    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None
    except ConnectionResetError:
        print("Connection was forcibly closed by the remote host.")
        return None
