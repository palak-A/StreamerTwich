
import requests
from twitch_streamer import constants

from twitch_streamer.twitch_api_handler.auth_handler import TwitchAuthHandler

class TwitchApiHandler():

	def __init__(self):
		self.twitch_auth_handler = TwitchAuthHandler()

	def get_channel_videos(self, channel_id):
		headers = self.twitch_auth_handler.get_headers()
		response = requests.get(url=constants.TWITCH_CHANNEL_URL.format(channel_id),headers=headers)

		videos  = self.parse_and_get_videos(response)

		return videos

	def get_user_id(self, username):
		user_url = constants.TWICH_GET_USER_URL.format(username)

		headers = self.twitch_auth_handler.get_headers()

		response = requests.get(url=user_url,headers=headers)

		user_id = self.parse_and_get_user_id(response)

		return user_id
	
	def parse_and_get_user_id(self, response):
		try:
			return response.json()['users'][0]['_id']
		except Exception as ex:
			print ex

		return None

	def parse_and_get_videos(self, response):
		try:
			return response.json()['videos']
		except Exception as ex:
			print ex
		return []
