from django.contrib import admin

# Register your models here.
from .models import Tutor, School, Course, UserInfo

class TutorAdmin(admin.ModelAdmin):
    list_display = ("name" , "price")

class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name" ,"city","state","zip_code")
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name" , "school_id", "department", "course_number")

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("LEVELS" , "first_name" , "last_name" , "email_TB" , "phone_TB" , "other_TB1" , "other_TB2", "school" , "level")

admin.site.register(Course, CourseAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(UserInfo, UserInfoAdmin)