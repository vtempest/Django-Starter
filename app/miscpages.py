from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *


def about(request):
  return render(request, 'miscpages/about.html',
      { 'username': request.user.username if request.user.is_authenticated() else "",
        'page_active': 0 })

def contact(request):
  return render(request, 'miscpages/contact.html',
      { 'username': request.user.username if request.user.is_authenticated() else "",
        'page_active': 0 })