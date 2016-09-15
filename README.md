# SlackBot_Reddit_Image_Poster
A Python Slack Bot which get latest image content from selected subreddits and post it to the selected channel.


Requirements
------------

| Requirements                        | Version/Comment |  URL                                          |
| ----------------------------------- |:---------------:|:---------------------------------------------:|
| SlackClient                         | 1.0.1           | https://github.com/slackhq/python-slackclient |
| PRAW: The Python Reddit Api Wrapper | >=3.5.0         | http://praw.readthedocs.io/en/stable/         |


Installation
------------
```
git clone https://github.com/Legionivo/SlackBot_Reddit_Image_Poster.git

cd SlackBot_Reddit_Image_Poster/

virtualenv %your_venv_name%

. %your_venv_name%/bin/activate

pip install -r requirements.txt 

export BOT_TOKEN="xxxxx-xxxx-xxxx"

export CHANNEL_ID="XXXXXXXXX" (or you can just use channel name like general, etc)

python slack_bot_reddit_image_poster.py

Enjoy! 

 ```
