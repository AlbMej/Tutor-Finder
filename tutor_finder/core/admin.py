from django.contrib import admin

# Register your models here.
from .models import Tutor, School, Course

class TutorAdmin(admin.ModelAdmin):
    list_display = ("name" , "price")

class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name" ,"city","state","zip_code")
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name" , "school_id", "department", "course_number")


admin.site.register(Course, CourseAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Tutor, TutorAdmin)