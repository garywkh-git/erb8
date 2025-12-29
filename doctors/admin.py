from django.contrib import admin
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = 'name','email','is_mvp','hire_date' #tuple
    list_display_links = 'name','email' #tuple
    list_editable = 'is_mvp', #tuple
    #list_fields = 'name', #tuple
    search_fields = 'name', #tuple
    list_per_page = 25

admin.site.register(Doctor, DoctorAdmin)