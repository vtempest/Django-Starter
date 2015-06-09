from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *

def reservation_read(request):

    if ReservationEntry.objects.count()==0:
        res = False
    else:
        res = ReservationEntry.objects.all()

    return render(request, 'reservation/reservation_read.html',  { 
        'page_active': 2,
        'username': request.user.username if request.user.is_authenticated() else "",
        
        'res': res  })


def reservation_delete(request):

    ReservationEntry.objects.filter(id=int(request.GET.get("reservation_id",""))).delete()
    return HttpResponse("Deleted")

def reservation_create(request):

    if len(request.GET.get("name", ""))==0 or len(request.GET.get("address", ""))==0 or len(request.GET.get("phone", ""))==0 or len(request.GET.get("time", ""))==0:
      return reservation_setup(request, error='Please fill out all the fields.' )


    r = ReservationEntry(
        name= request.GET.get("name", ""),
        address= request.GET.get("address", ""),
        phone= request.GET.get("phone", ""),
        time= request.GET.get("time", "")
    )

    if TableEntry.objects.filter(title__iexact=request.GET.get("table", "")).count()==0:
        return reservation_setup(request, error='No tables available.' )

    if ReservationEntry.objects.filter(table=TableEntry.objects.get(title__iexact=request.GET.get("table", ""))).count()>0:
        return reservation_setup(request, error='That table is unavailable.' )

    r.table = TableEntry.objects.get(title__iexact=request.GET.get("table", ""))

    r.save()

    for FoodEntryTitle in request.GET.getlist("foodlist", ""):
        r.foodList.add(FoodEntry.objects.get(title=FoodEntryTitle))

    r.save()

    return render(request, 'reservation/reservation_success.html', { 
        'res': request.GET  })


def reservation_setup(request, **kwargs):

    error = kwargs['error'] if len(kwargs)>0 else ""

    TableListEmpty = []
    for TableEntryObject in TableEntry.objects.all():
        if ReservationEntry.objects.filter(table=TableEntryObject).count() == 0:
            TableListEmpty.append(TableEntryObject.title)
    if len(TableListEmpty)==0:
        TableListEmpty = False

    return render(request, 'reservation/reservation_create.html', {
        'page_active': 1,
        'username': request.user.username if request.user.is_authenticated() else "",
        'error': error,
        'FoodList': FoodEntry.objects.all(),
        'TableList': TableListEmpty
    })