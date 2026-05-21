from django.contrib import admin
from .models import Project, Step, AsanaProject

# Register your models here.
admin.site.register(Project)
admin.site.register(Step)
admin.site.register(AsanaProject)