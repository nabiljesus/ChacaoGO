from django.contrib import admin

from main.models import User,Event,Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Comment)
