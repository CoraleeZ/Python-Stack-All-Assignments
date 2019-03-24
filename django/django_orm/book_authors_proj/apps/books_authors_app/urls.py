from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^books/(?P<idbook>[0-9]+)$',views.indexshow),
    url(r'^addbooks$',views.addbooks),
    url(r'^addauthorforb/(?P<idbook>[0-9]+)$',views.addauthorforb),
    url(r'^authors$',views.authorsadd),
    url(r'^authors/(?P<idauthor>[0-9]+)$',views.authorshow),
    url(r'^addauthors$',views.addauthors),
    url(r'^addbookfora/(?P<idauthor>[0-9]+)$',views.addbookfora),
]