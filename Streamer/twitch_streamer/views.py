# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from twitch_streamer import constants
from twitch_streamer.twitch_api_handler import TwitchAuthHandler
from twitch_streamer.twitch_api_handler import TwitchApiHandler

# Create your views here.
def index(request):
	twitch_auth_handler = TwitchAuthHandler()
	auth_redirect_url = twitch_auth_handler.get_auth_redirect_url()
	return render_to_response('index.html', {"auth_redirect_url": auth_redirect_url})

def getAuthorization(request):
	auth_url = constants.TWITCH_AUTH_URL + "?client_id={}&response_type={}&redirect_uri={}".format(
		settings.CLIENT_ID, constants.RESPONSE_TYPE, constants.REDIRECT_URI
	)
	resp = requests.post(token_url)	

def getToken(request):
	code = request.GET.get('code', None)

	twitch_auth_handler = TwitchAuthHandler()
	resp = twitch_auth_handler.fetch_access_token(code)
	return render_to_response('home.html', {'events': [], 'found': False})

def getVideo(request):
	body = request.body
	if not body:
		return render_to_response('home.html', {'events': [], 'found': False})
	
	username = body.split('=')[1]
	twitch_api_handler = TwitchApiHandler()
	channel_id = twitch_api_handler.get_user_id(username)

	if not channel_id:
		print "Channel ID: {} not found for username".format(username)
		return render_to_response('home.html', {'events': [], 'found': False})
	videos = twitch_api_handler.get_channel_videos(channel_id)
	return render_to_response('home.html', {'videos': videos, 'found': True, 'username': username})

def getStreamer(request):
	user_url = 'https://api.twitch.tv/kraken/users?login={}'.format(username)
	return channels

	
