from django.contrib import admin
from .models import (
    Faculty, Speciality, Subject, Language, StudentStatus, News, Notification,
    Application, ApplicationStatus, Student
)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('formatted_id', 'last_name', 'first_name', 'middle_name', 'faculty', 'speciality', 'status')

    def formatted_id(self, obj):
        return f"{obj.id:06d}"

    formatted_id.short_description = 'ID'

admin.site.register(Student, StudentAdmin)

class StudentInline(admin.StackedInline):
    model = Student
    extra = 1

class FacultyAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

class SpecialityAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

class StudentStatusAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(StudentStatus, StudentStatusAdmin)
admin.site.register(Subject)
admin.site.register(Language)
admin.site.register(News)
admin.site.register(Notification)
admin.site.register(Application)
admin.site.register(ApplicationStatus)




# admin.site.register(Faculty)
# admin.site.register(Speciality)
# admin.site.register(Subject)
# admin.site.register(Language)
# admin.site.register(StudentStatus)
# admin.site.register(News)
# admin.site.register(Notification)
# admin.site.register(Application)
# admin.site.register(ApplicationStatus)
# admin.site.register(Student)
