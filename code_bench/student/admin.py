from django.contrib import admin

# Register your models here.
from .  import models

admin.site.register(models.Course)
admin.site.register(models.Student)
admin.site.register(models.Exam)
admin.site.register(models.ObjectiveQuestion)
admin.site.register(models.SubjectiveQuestion)
admin.site.register(models.ObjectiveAnswer)
admin.site.register(models.SubjectiveAnswer)




