from django.contrib import admin

# Register your models here.

from .models import *

admin.site.site_header='Movie Club || Admin'
admin.site.register(Movie)
admin.site.register(Movielist)
admin.site.register(Genre)