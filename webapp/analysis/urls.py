# analysis/urls.py

from django.conf.urls import url
from analysis import views

# SET THE NAMESPACE!
app_name = 'analysis'

urlpatterns=[
    url(r'^twitter/$',views.analysis_twitter,name='twitter'),
    url(r'^tumblr/$',views.analysis_tumblr,name='tumblr'),
    url(r'^graphs/(?P<analysis_type>\w{0,20})/$',views.graphs,name='graphs'),
    url(r'^graphs_tumblr/(?P<analysis_type>\w{0,20})/$',views.graphs_tumblr,name='graphs_tumblr'),
    url(r'^twitter/view_tweets/$',views.view_tweets,name='twitter/view_tweets'),
    url(r'^tumblr/view_posts/$',views.view_tumblr_posts,name='tumblr/view_tumblr_posts'),
    url(r'^export_csv/', views.export_csv, name='export_csv'),
    url(r'^export_excel/', views.export_excel, name='export_excel'),
    url(r'^exports/', views.exports, name='exports'),
    url(r'^export_clicked/', views.export_clicked, name='export_clicked'),
    # url(r'^graph/$', views.graph, name = 'graph'),
    # url(r'^create_analysis/',views.create_analysis,name='create_analysis'),
]

