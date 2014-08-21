from django.conf.urls import patterns, url
from shop import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
	url(r'^newest/$', views.index2, name='index'),
	url(r'^add/', views.addItem, name='Add'),
	url(r'^item/(?P<salePage>\d+)/$', views.salePage, name='selling'),
        #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
        #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
        #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),)
)
