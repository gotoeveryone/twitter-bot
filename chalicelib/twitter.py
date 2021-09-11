
import boto3
from requests.models import Response
from requests_oauthlib import OAuth1Session


class TwitterClient:
    def __init__(self):
        self._ssm = boto3.client('ssm')

        twitter_consumer_key = self.get_parameter('twitter_consumer_key')
        twitter_consumer_secret = self.get_parameter('twitter_consumer_secret')
        twitter_access_token = self.get_parameter('twitter_access_token')
        twitter_access_token_secret = self.get_parameter('twitter_access_token_secret')

        self._client = OAuth1Session(
            twitter_consumer_key,
            twitter_consumer_secret,
            twitter_access_token,
            twitter_access_token_secret,
        )

    def send(self, message: str) -> Response:
        """
        Send message to Twitter
        """
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        return self._client.post(url, params={
            'status': message,
        })

    def get_parameter(self, key: str) -> str:
        """
        Get value from Parameter Store
        """
        response = self._ssm.get_parameter(
            Name=key,
            WithDecryption=True
        )
        return response['Parameter']['Value']
