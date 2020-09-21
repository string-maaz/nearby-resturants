import re
from django.conf import settings
from django.urls ifmport reverse
from django.shortcuts import redirect
from django.contrib.auth import logout


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class loginMiddleware(object):
	def __call__(self, request):
		print "ok"
		response = self.get_response(request)
		print 'request completed'
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		assert hasattr(request, 'user')
		path = request.path_info.lstrip('/')
		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

		# if path == reverse('website:home').lstrip('/'):
		# 	logout(request)
		print url_is_exempt, request.user.is_authenticated()

		if request.user.is_authenticated() and url_is_exempt:
			return redirect(settings.LOGIN_REDIRECT_URL)
		elif request.user.is_authenticated() or url_is_exempt:
			return None
		else:
			return redirect(settings.LOGIN_URL_NEW)
