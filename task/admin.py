from django.contrib import admin
from .models import Ts
@admin.register(Ts)
class TsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'done']

