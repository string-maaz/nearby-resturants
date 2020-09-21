# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.http import HttpResponse,HttpResponseRedirect
import json
# import urllib.request, urllib.error, urllib.parse
import urllib2


def nearby_resturants(request):
    data = {}
    # print data
    return render(request,'base_templates/layout/nearby_resturants.html',{"data":data})

def hit_url(url):
	# url = urllib2.quote(url)
	response = urllib2.urlopen(url).read()
	# response = urllib.request.urlopen(url).read()
	return response

def get_place_from_latlng(lat,lng):
	try:
		# 2 decimal precision for detecting up to small towns and villages (up to 1 KM)
		precision = 2
		round_lat = round(float(lat), precision)
		round_lng = round(float(lng), precision)
		lat_lng = str(lat)+","+str(lng)
		url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat_lng+"&radius=50000&type=region&key=" + settings.GOOGLE_LOCATION_API_KEY
		response = hit_url(url)

		url_response_dict = json.loads(response)
		return url_response_dict

	except Exception as e:
		print e
		return None

def process_user_location(request):
	is_geo_data_available = request.GET.get('isGeoDataAvailable')
	if is_geo_data_available == 'true':
		place = get_place_from_latlng(request.GET.get('lat'),request.GET.get('lng'))
		print place



