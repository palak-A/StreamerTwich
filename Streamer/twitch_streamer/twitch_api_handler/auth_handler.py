
# Standard python imports

import uuid
import requests
from datetime import datetime
# Project imports
from django.conf import settings
#xfrom django.conf.settings import CLIENT_ID, CLIENT_SECRET

from twitch_streamer import constants 

_auth_info = {
	"access_token" : None,
	"refresh_token" : None,
	"expires_in" : None,
	"token_type" : None,
	"token_requested_time": None
}


class TwitchAuthHandler():

	def validate_response(self, response):
		if response.status_code == 200:
			return True

		return False

	def get_client_id(self):
		return settings.CLIENT_ID

	def get_client_secret(self):
		return settings.CLIENT_SECRET

	def get_redirect_uri(self):
		return constants.REDIRECT_URI

	def get_auth_redirect_url(self):
		auth_url = constants.TWITCH_AUTH_URL
		client_id = self.get_client_id()
		response_type = constants.RESPONSE_TYPE
		redirect_uri = self.get_redirect_uri()
		state = uuid.uuid4()

		auth_redirect_url = "{}?client_id={}&response_type={}&redirect_uri={}&state={}".format(
			auth_url, client_id, response_type, redirect_uri, state
		)

		return auth_redirect_url

	def get_token_url(self, code):

		token_url = constants.TWITCH_TOKEN_URL + "?client_id={}&client_secret={}&code={}&grant_type={}&redirect_uri={}".format(
			settings.CLIENT_ID, settings.CLIENT_SECRET, code, constants.GRANT_TYPE, constants.REDIRECT_URI
	    	)

		return token_url

	def fetch_access_token(self, code):
		token_url = self.get_token_url(code)
		resp = requests.post(token_url)

		#self.validate_response(resp)
		is_succ_parsing = self.parse_store_token(resp)

		if is_succ_parsing:
			return _auth_info['access_token']
		
		return None

	def parse_store_token(self, resp):
		json_resp = resp.json()

		access_token = json_resp['access_token']
		refresh_token = json_resp['refresh_token']
		expires_in = json_resp['expires_in']
		token_type = json_resp['token_type']

		_auth_info['access_token'] = access_token
		_auth_info['refresh_token'] = refresh_token
		_auth_info['expires_in'] = expires_in
		_auth_info['token_type'] = token_type
		_auth_info['token_requested_time'] = datetime.now()

		print _auth_info

		return True

	def get_headers(self):
		headers = {
					'Accept': 'application/vnd.twitchtv.v5+json',
 					'Authorization': 'OAuth {}'.format(_auth_info['access_token']),
 					'Client-ID': 'constants.CLIENT_ID',
 					'Content-Type': 'application/json',
 					# 'scope': 'channel_editor',
 					# 'scopes': '&scope=channel_check_subscription'
 					}

 		return headers

	# def get_access_token(self):
	# 	return token

	# def get_channels(self):
	# 	user_url = 'https://api.twitch.tv/kraken/users?login={}'.format('palak03')
	# 	return channels

	# def get_events(self):
	# 	client_id = self.get_client_id()
	# 	event_url = 'https://api.twitch.tv/kraken/channels/83402203/videos'