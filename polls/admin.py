from django.contrib import admin

# Register your models here.

from .models import Import
from .models import Slice

admin.site.register(Import)
admin.site.register(Slice)