from slackclient import SlackClient
import praw
from time import sleep
import random
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

CHANNEL_ID = os.getenv('CHANNEL_ID')  # channel ID, or just use channel name

def get_posts(subreddit):
    user_agent = ("User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0")
    r = praw.Reddit(user_agent=user_agent)
    subreddit = r.get_subreddit(subreddit)
    url_list = []
    for submission in subreddit.get_new(limit=100):  # get 100 new submissions
        url_list.append(str(submission.url))
    return url_list

def random_pic_choice(ul=get_posts()):
    i = random.choice(ul)
    ul.remove(i)
    return i
    

def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)
    # Connect to slack
    if sc.rtm_connect():

        while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                if slack_message.get("channel") != CHANNEL_ID:
                    break
                message = slack_message.get("text")
                if message == "!help":
                    sc.rtm_send_message(CHANNEL_ID,
                                        " It's time to have fun!!! I'm pulling the newest fun content from reddit. "
                                        " The following commands are currently supported: `!pics, !funny, !cats`. "
                                        " Enjoy watching :)")
                subreddits = (
                    'pics', 'funny', 'cats')
                for key in subreddits:
                    if message == "!" + key:
                        sc.rtm_send_message(CHANNEL_ID, random_pic_choice(str(key)))
                user = slack_message.get("user")
                if not message or not user:
                    continue
            # Sleep for half a second
            sleep(0.5)


if __name__ == '__main__':
    main()
