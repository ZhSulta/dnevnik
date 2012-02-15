from django.contrib import admin
from apps.models.models import City,Parent,Organization,ParentProfile,School,Student,StudentProfile,Teacher,TeacherProfile


class StudentAdmin(admin.ModelAdmin):
    fieldset =  [
        ('full name',   {'fields':{'name','surname'}}),
        ('school',      {'fields':{'school'}})
    ]

    
    
admin.site.register(City)
admin.site.register(Parent)
admin.site.register(Organization)
admin.site.register(ParentProfile)
admin.site.register(School)
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentProfile)
admin.site.register(Teacher)
admin.site.register(TeacherProfile)


