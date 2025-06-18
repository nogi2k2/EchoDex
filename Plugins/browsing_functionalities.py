import webbrowser 
import re
import wikipedia
import speedtest
from youtubesearchpython import VideoSearch
import websites

def cleaned_query(query):
    pattern = r'\b(images?|search|show|google|tell me about|for|of)\b'
    cleaned_query = re.sub(pattern, '', query, flags = re.IGNORECASE)
    return re.sub(r'\s+', ' ', cleaned_query).strip()

def googleSearch(query):
    if 'image' in query.lower():
        query += '&tbm=isch'
    
    query = cleaned_query(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return "Opening Browser"

def youtube(query):
    pattern = r'\b(play|on youtube|youtube)\b'
    query = re.sub(pattern, ' ', query, flags = re.IGNORECASE)
    query = re.sub(r'\s+', ' ', query).strip()
    print("Video lookup in progress")
    videoSearch = VideoSearch(query, limit = 1)
    result = videoSearch.result()['result'][0]['id']
    webbrowser.open(f"https://www.youtube.com/watch?v="{query})
    return f"Opening Youtube Video"

def open_specified_website(query):
    website = query[5:]
    if website in websites.websites_dict:
        url = websites.websites_dict[website]
        webbrowser.open(url)
        return True
    else:
        return None
    
def get_speedtest():
    try:
        st = speedtest.Speedtest()
        speed = f"Network Download Speed: {round(st.download()/ 8388608, 2)} MBps\n"\
        f"Network Upload Speed: {round(st.upload()/ 8388608, 2)} MBps"
        return speed
    except (KeyboardInterrupt, speedtest.SpeedtestException) as e:
        return 
    
def tell_me_about(query):
    try:
        query = query.replace("tell me about ", "") 
        summary = wikipedia.summary(query, sentences = 3)
        summary = re.sub(r'\[.*?\]', "", summary)
        return summary
    except (Exception, wikipedia.WikipediaException) as e:
        return None
    
def get_map(query):
    webbrowser.open(f"https://www.google.com/maps/search/{query}")
