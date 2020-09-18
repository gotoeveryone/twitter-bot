import json
import os
import random
import boto3
from chalice import Chalice, Cron
from requests_oauthlib import OAuth1Session

app = Chalice(app_name='twitter-bot')
app.debug = True if os.getenv('DEBUG', False) else False


def get_message():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('bot_messages')
    result = table.scan()
    if not result['Items']:
        return 'It''s default message.'
    item = random.choice(result['Items'])

    return item['message']


def update_status():
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    twitter = OAuth1Session(
        os.getenv('CONSUMER_KEY'),
        os.getenv('CONSUMER_SECRET'),
        os.getenv('ACCESS_TOKEN'),
        os.getenv('ACCESS_TOKEN_SECRET'),
    )
    res = twitter.post(url, params={
        'status': get_message(),
    })

    return {
        'code': res.status_code,
        'body': res.json(),
    }


@app.schedule(Cron(0, 23, '?', '*', '*', '*'))
def lambda_handler(event, context={}):
    return update_status()
