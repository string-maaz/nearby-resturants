# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
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

class SingleLocationView(TemplateView):
    template_name = 'base_templates/layout/nearby_resturants.html'
    post_template_name = 'base_templates/layout/resturants_list.html'


    def get_context_data(self, **kwargs):
        request_type = self.request.method
        if request_type == 'GET':
            kwargs['teams'] = Team.objects.filter(is_active = True)
        elif request_type == 'POST':
            location_id = int(self.request.POST.get('location'))
            # print 'team id ',location_id
            kwargs['resturants'] = Resturant.objects.filter(location_id = location_id, is_active = True).order_by('id')
            kwargs['total_resturnats'] = MatchPoint.objects.filter(location_id = location_id, is_active = True).count()
        return super(SingleLocationView,self).get_context_data(**kwargs)


    def get_template_names(self):
        if self.template_name is None:
                raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        elif self.request.method == 'GET':
            return [self.template_name]
        elif self.request.method == 'POST':
            return [self.post_template_name]


    def post(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        # print context
        data = {}
        data['html'] = render_to_string(self.get_template_names()[0],context)
        data['resturant'] = self.request.POST.get('resturant')
        return HttpResponse(json.dumps(data),content_type="application/json")
	

