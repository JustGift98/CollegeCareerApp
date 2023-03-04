from django.contrib import admin
from . models import GradStudent, College, StudyProgram


# Register your models here.
admin.site.register(GradStudent)
admin.site.register(College)
admin.site.register(StudyProgram)