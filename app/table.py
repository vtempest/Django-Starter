from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *

def table_delete(request):
    TableEntry.objects.filter(title__iexact=request.GET.get("table_name","")).delete()
    return HttpResponse("Deleted "+request.GET.get("table_name",""))
 
def table_create(request):
    t = TableEntry.objects.create(title=request.GET.get("table_name",""))
    t.save()
    return HttpResponse("Created "+request.GET.get("table_name",""))

def table_read(request):
    TableList = []
    for TableEntryObject in TableEntry.objects.all():
        if ReservationEntry.objects.filter(table=TableEntryObject).count() == 0:
           TableList.append({'table': TableEntryObject.title, 'reserved': ''})
        else:
            TableList.append({'table': TableEntryObject.title, 'reserved': ReservationEntry.objects.get(table=TableEntryObject).name })

    return render(request, 'table/table_read.html',{ 
        'page_active': 3,
          'username': request.user.username if request.user.is_authenticated() else "",
          'res': TableList })