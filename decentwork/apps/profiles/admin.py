from django.contrib import admin

from .models import Rating, UserProfile

admin.site.register(UserProfile)
admin.site.register(Rating)