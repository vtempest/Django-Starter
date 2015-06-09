from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.shortcuts import *
from app.models import *


def food_create(request):

    f = FoodEntry.objects.create(title=request.GET.get("food_name",""), price=request.GET.get("food_price",""))
    f.save()
    return HttpResponse("Created " + request.GET.get("food_name",""))

def food_delete(request):

    FoodEntry.objects.filter(title__iexact=request.GET.get("food_name","")).delete()
    return HttpResponse("Deleted " + request.GET.get("food_name",""))
 
def food_read(request):
  
  FoodEntryAll = FoodEntry.objects.all()

  return render(request, 'food/food_read.html',      { 
  	'page_active': 4,
  	'username': request.user.username if request.user.is_authenticated() else "",
        

      'res': FoodEntryAll })