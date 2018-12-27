from django.contrib import admin

from .models import Notice, UserAssigned

admin.site.register(Notice)
admin.site.register(UserAssigned)
