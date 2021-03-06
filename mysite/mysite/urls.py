from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from mysite import settings
import shop

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^shop/', include('shop.urls', namespace="shop")),
(r'^accounts/login/$', "django.contrib.auth.views.login", {'template_name': 'polls/login.html'}),
(r'^accounts/create/$', shop.views.create),
(r'^accounts/logout/$', "django.contrib.auth.views.logout", {'next_page': '/shop/'}),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)


