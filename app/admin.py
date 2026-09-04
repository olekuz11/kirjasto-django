from django.contrib import admin
from .models import Kirjailija, Kirja, Laina

admin.site.register(Kirjailija)
admin.site.register(Kirja)
admin.site.register(Laina)