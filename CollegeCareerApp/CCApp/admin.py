from django.contrib import admin
from . models import GradStudent, College, StudyProgram, Offering


# Register your models here.
admin.site.register(GradStudent)
admin.site.register(College)
admin.site.register(StudyProgram)
admin.site.register(Offering)