from django.contrib import admin
from .models import Board, Note

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name'] 

# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(Note)
