from django.contrib import admin

from app1.models import Reg
class reg1(admin.ModelAdmin):
          list_display=['Student_name','Student_roll','student_marks']
admin.site.register(Reg,reg1)
