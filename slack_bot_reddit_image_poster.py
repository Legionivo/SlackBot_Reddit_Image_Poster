from slackclient import SlackClient
import praw
from time import sleep
import random
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

CHANNEL_ID = os.getenv('CHANNEL_ID')  # channel ID, or just use channel name

subreddits = ('pics', 'funny', 'cats', 'aww', 'gifs')

help_message = " It's time to have fun!!! I'm pulling the newest fun content from reddit.The following commands" \
               " are currently supported:" + "`" + "!" + ", !".join(subreddits) + "`" + \
               " And type " + "`" + "!command new" + "`" + " to get *newest* pictures! " \
               " And type " + "`" + "!command some_number from 2 to 10 (new also acceptable)" + "`" + " to get *several* pictures! " \
               " Thanks for watching :)"
   
  
def get_posts(subreddit, position):
    user_agent = ("User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0")
    r = praw.Reddit(user_agent=user_agent)
    try:
        subreddit = r.get_subreddit(subreddit)
        url_list = []
        if position == "new":
            for submission in subreddit.get_new(limit=100):  # get 100 new submissions
                url_list.append(str(submission.url))
            return random.choice(url_list)
        elif position == "hot":
            for submission in subreddit.get_hot(limit=100):  # get 100 hot submissions
                url_list.append(str(submission.url))
            return random.choice(url_list)
    except (praw.errors.PRAWException, praw.errors.HTTPException) as e:
        print e
        pass


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
                user = slack_message.get("user")
                if not message or not user:
                    continue
                if message == "!help":
                    sc.rtm_send_message(CHANNEL_ID, help_message)
                                for key in subreddits:
                    if message == "!" + key:
                        sc.rtm_send_message(CHANNEL_ID, get_posts(str(key), "new"))
                    if message == "!" + key + " hot":
                        sc.rtm_send_message(CHANNEL_ID, get_posts(str(key), "hot"))
        # Sleep for half a second
        sleep(0.5)


if __name__ == '__main__':
    main()
