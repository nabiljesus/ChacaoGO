from django.contrib import admin
from main.models import User,Event,Comment,Category

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Comment)