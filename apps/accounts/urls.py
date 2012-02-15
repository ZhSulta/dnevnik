from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('accounts.views',
     url(r'school_reg/$', 'school_reg', name = 'school_reg'),
     url(r'parents_reg/$', 'parents_reg', name = 'parents_reg'),
     url(r'students_reg/$', 'students_reg', name = 'students_reg'),
     url(r'teachers_reg/$', 'teachers_reg', name = 'teachers_reg'),
     
)

