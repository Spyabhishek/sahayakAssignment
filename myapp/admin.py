from django.contrib import admin
from .models import student,teacher
# Register your models here.

class teacherAdmin(admin.ModelAdmin):
    list_display=['teacher_id','name']

class studentAdmin(admin.ModelAdmin):
    list_display=['student_id','name','taught_by']    

admin.site.register(student,studentAdmin)
admin.site.register(teacher,teacherAdmin)
