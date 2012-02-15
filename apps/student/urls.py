from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('student.views',
    url(r'^$', 'index'),    
)

