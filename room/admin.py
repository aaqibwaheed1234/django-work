from django.contrib import admin

# Register your models here.
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display=['room','user', 'content', 'date_added']

admin.site.register(Message,MessageAdmin)
