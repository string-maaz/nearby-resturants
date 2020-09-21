from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import LoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse
from resturants.settings import LOGIN_REDIRECT_URL
from django.http import HttpResponse,HttpResponseRedirect
import json



class LoginView(FormView):
	template_name = 'base_templates/layout/login.html'
	form_class = LoginForm
	success_url = 'base_templates/layout/dashboard/'
	def get(self,request,*args,**kwargs):
		# if request.user.is_authenticated():
		# 	return redirect(reverse(LOGIN_REDIRECT_URL))
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		context = self.get_context_data(**kwargs)
		context['form'] = form
		return self.render_to_response(context)

	def post(self,request,*args,**kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		return self.is_valid(form)

	def is_valid(self,form):
		username = form.data['username']
		password = form.data['password']
		user = authenticate(username=username,password=password)
		if user and user.is_authenticated():
			login(self.request,user)
			return redirect(reverse(LOGIN_REDIRECT_URL))
		else:
			form.add_error("password","Username and Password does not match")
			if form.errors.get('username'):
				del form.errors['username']
			return self.form_invalid(form)


def dashboard(request):
    data = {}
    # print data
    return render(request,'base_templates/layout/dashboard.html',{"data":data})