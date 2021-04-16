from django.contrib import admin


# Register your models here.


from .models import User
from .models import Reto

admin.site.register(User)
admin.site.register(Reto)
