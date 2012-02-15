from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('teacher.views',
    url(r'^$', 'index'),    
)

