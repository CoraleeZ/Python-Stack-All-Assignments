from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^shows/new$',views.new),
    url(r'^shows/create$',views.create),
    url(r'^shows/(?P<showid>[0-9]+)$',views.showinfo),
    url(r'^shows$',views.showall),
    url(r'^shows/(?P<editid>[0-9]+)/edit$',views.edit),
    url(r'^shows/(?P<updateid>[0-9]+)/update$',views.update),
    url(r'^shows/(?P<deleteid>[0-9]+)/destroy$',views.delete),
]