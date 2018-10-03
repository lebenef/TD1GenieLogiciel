from django.contrib import admin

# Register your models here.

from .models import Classe

from .models import Ordre

from .models import Famille

from .models import Animal



admin.site.register(Classe)

admin.site.register(Ordre)

admin.site.register(Famille)

admin.site.register(Animal)
