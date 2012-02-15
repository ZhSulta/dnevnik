from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('student.views',    
    url(r'^(?P<student_id>\d+)/$', 'student_main', name = 'student_main'),
    url(r'^profile/(?P<student_id>\d+)/$', 'student_profile', name = 'student_profile'),    
)

