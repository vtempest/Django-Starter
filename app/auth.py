from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import *



def members(request):
	if request.user.is_authenticated():
		return HttpResponse("Hello "+request.user.username)
	else:
		return HttpResponse("Access denied")


def user_logout(request):
	logout(request)
	return HttpResponse("Logged out")

def user_register(request):
   	
	username = request.GET.get("username","")
	password = request.GET.get("password","")

	if User.objects.filter(username=username).count()>0:
		return HttpResponse("Taken")


	user = User.objects.create_user(username=username,password=password)
	user.save()

	#auto sign in
	user = authenticate(username=username, password=password)
	login(request, user)


	return HttpResponse("Registered")


def user_login(request):

	username = request.GET.get("username","")
	password = request.GET.get("password","")

	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponse("Success")  
	else:
		return HttpResponse("Invalid")