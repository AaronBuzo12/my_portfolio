from django.contrib import admin

# Register your models here.
from .models import Project, ContactMessage

admin.site.register(Project)
admin.site.register(ContactMessage)