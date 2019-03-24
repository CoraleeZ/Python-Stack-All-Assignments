from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^books$',views.bookshome),
    url(r'^logout$',views.logout),
    url(r'^books/add$',views.addbook),
    url(r'^addbookprocess$',views.addbookprocess),
    url(r'^books/(?P<bookid>[0-9]+)$',views.booksinfo),
    url(r'^reviewprocess/(?P<bookid_addreview>[0-9]+)$',views.reviewprocess),
    url(r'^users/(?P<userid>[0-9]+)$',views.userinfo),
    ]