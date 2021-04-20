from django.contrib import admin


# Register your models here.


from .models import User
from .models import Reto

from .models import Level
from .models import Engranes
from .models import Session
from .models import Recompensas
from .models import Try


admin.site.register(User)
admin.site.register(Reto)


admin.site.register(Level)
admin.site.register(Engranes)
admin.site.register(Session)
admin.site.register(Recompensas)
admin.site.register(Try)

