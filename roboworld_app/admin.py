from django.contrib import admin


# Register your models here.


from .models import Reto
from .models import Level
from .models import Engranes
from .models import Sesion
from .models import Recompensas
from .models import Prueba

from .models import Perfil


admin.site.register(Reto)
admin.site.register(Level)
admin.site.register(Engranes)
admin.site.register(Sesion)
admin.site.register(Recompensas)
admin.site.register(Prueba)

admin.site.register(Perfil)
