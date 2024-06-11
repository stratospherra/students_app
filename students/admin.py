from django.contrib import admin
from .models import (
    Faculty, Speciality, Subject, Language, StudentStatus, News, Notification,
    Application, ApplicationStatus, Student
)

admin.site.register(Faculty)
admin.site.register(Speciality)
admin.site.register(Subject)
admin.site.register(Language)
admin.site.register(StudentStatus)
admin.site.register(News)
admin.site.register(Notification)
admin.site.register(Application)
admin.site.register(ApplicationStatus)
admin.site.register(Student)
