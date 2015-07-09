from django.contrib import admin
from main.models import User,Event,Comment,Category,Vote

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Vote)