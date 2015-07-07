from django.contrib import admin
<<<<<<< HEAD

from main.models import User,Event,Comment
=======
from main.models import User,Event,Comment,Category
>>>>>>> 8ab41d4160ed93b3c869fc02415f020c4d6cf83b

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
<<<<<<< HEAD
admin.site.register(Comment)
=======
admin.site.register(Category)
admin.site.register(Comment)
>>>>>>> 8ab41d4160ed93b3c869fc02415f020c4d6cf83b
