import json
import requests


def get_meme():
    # sr = "wholesomememes"
    # url = "https://meme-api.herokuapp.com/gimme" + sr
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit
