from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('guest.views',
    url(r'^$', 'index'),    
)

