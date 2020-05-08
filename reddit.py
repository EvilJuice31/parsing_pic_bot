import os

import praw
import random
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
user_agent = os.getenv('user_agent')
username = os.getenv('user')
password = os.getenv('password')


r = praw.Reddit(client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent,
                username=username,
                password=password)


def get_pic():
    subs = ['funny', 'pics', 'BeAmazed']
    sub = random.choice(subs)
    result = r.subreddit(sub).random().url
    if 'jpg' in result or 'png' in result:
        return result
    else:
        return get_pic()
