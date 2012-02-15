from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('org.views',
    url(r'^$', 'index'),    
)

