from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('school.views',
    url(r'^$', 'index'),    
)

