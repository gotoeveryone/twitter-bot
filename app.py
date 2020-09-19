import json
import os
import random

import boto3
from chalice import Chalice, Cron
import requests
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


def notify(webhook_url: str, subject: str, message: str):
    if app.debug:
        app.log.info(message)
    else:
        requests.post(webhook_url, data=json.dumps({
            'text': f'{subject}```{message}```',
            'username': 'twitter-bot',
        }))


def update_status():
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    twitter = OAuth1Session(
        os.getenv('CONSUMER_KEY'),
        os.getenv('CONSUMER_SECRET'),
        os.getenv('ACCESS_TOKEN'),
        os.getenv('ACCESS_TOKEN_SECRET'),
    )
    message = get_message()

    res = twitter.post(url, params={
        'status': message,
    })

    webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    if webhook_url:
        if res.status_code != 200:
            subject = '*Status update failed*'
            errors = res.json().get('errors', [])
            error_message = errors[0].get('message') if errors else 'Unknown Error'
            message = f'Cause: {error_message}'
        else:
            subject = '*Status update successful*'
            message = f'Message: "{message}"'

        notify(webhook_url, subject, message)

    return {
        'code': res.status_code,
        'body': res.json(),
    }


@app.schedule(Cron(30, 14, '*', '*', '?', '*'))  # UTC 14:30 -> JST 23:30
def lambda_handler(event, context={}):
    return update_status()
