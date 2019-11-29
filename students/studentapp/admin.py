from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'Student Management'
admin.site.site_title = 'Students App'
admin.site.index_title = 'Student Home'
admin.site.register(Student)
