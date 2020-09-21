from django.conf.urls import url,include
from location.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nearby_resturants/$',login_required(nearby_resturants),name='nearby_resturants'),
    url(r'^process-user-place/$',login_required(process_user_location),name='process_user_location'),

    ]