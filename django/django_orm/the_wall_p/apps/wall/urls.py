from django.conf.urls import url
from. import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^mainwall$',views.mainwall),
    url(r'^logout$',views.logout),
    url(r'^login$',views.login),
    url(r'^addmessage$',views.addmessage),
    url(r'^wall$',views.wall),
    url(r'^addcomment$',views.addcomment),
    url(r'^deletemessage/(?P<messageid>[0-9]+)$',views.deletemessage),
    url(r'^deletecomment/(?P<commentid>[0-9]+)$',views.deletecomment),
]