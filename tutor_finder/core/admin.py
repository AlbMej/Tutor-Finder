from django.contrib import admin

# Register your models here.
from .models import Tutor

class TutorAdmin(admin.ModelAdmin):
    list_display = ("name" , "price")

admin.site.register(Tutor, TutorAdmin)