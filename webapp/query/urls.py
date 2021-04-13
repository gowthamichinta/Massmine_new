# query/urls.py

from django.conf.urls import url
from query import views

# SET THE NAMESPACE!
app_name = 'query'

# Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    url(r'^twitter/$', views.twitter, name='twitter'),
    url(r'^tumblr/$', views.tumblr, name='tumblr'),
    url(r'^make_query/$', views.make_query, name='make_query'),
    url(r'^make_query_tumblr/$', views.make_query_tumblr, name='make_query_tumblr'),
    url(r'^platforms/$', views.platforms, name='platforms'),
    url(r'^platforms/$', views.platforms1, name='platforms1'),

]
