from django.contrib import admin
from .models import Party, Vote

# Register your models here.

admin.site.register([Party, Vote])
