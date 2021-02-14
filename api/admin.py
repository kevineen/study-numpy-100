from django.contrib import admin

# Register your models here.
from .models import Task, Employee, Department

admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Department)
