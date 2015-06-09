from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import *

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', "app.reservation.reservation_setup", name="index"),


	
	url(r'login$', "app.auth.user_login", name="login"),
	url(r'logout$', "app.auth.user_logout", name="logout"),
	url(r'register$', "app.auth.user_register", name="register"),

	url(r'reservation/create$', "app.reservation.reservation_create", name="reservation_create"),
	url(r'reservation/delete$', "app.reservation.reservation_delete", name="reservation_delete"),
	url(r'reservation$', "app.reservation.reservation_read", name="reservation_read"),

	url(r'table$', "app.table.table_read", name="table_read"),
	url(r'table/create$', "app.table.table_create", name="table_create"),
	url(r'table/delete$', "app.table.table_delete", name="table_delete"),

	url(r'food$', "app.food.food_read", name="food_read"),
	url(r'food/create$', "app.food.food_create", name="food_create"),
	url(r'food/delete$', "app.food.food_delete", name="food_delete"),

	url(r'about$', "app.miscpages.about", name="about"),
	url(r'contact$', "app.miscpages.contact", name="contact"),
 	
)
