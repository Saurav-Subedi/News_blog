from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=['name','slug','order','show_image']
    prepopulated_fields={'slug':('name',)}
    list_editable=['order']
    search_fields=['name','slug']

    def show_image(self,obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="80"/>')
        else:
            return 'No Image'

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display=['title','category','show_image','is_banner','created_at']
    prepopulated_fields={'slug':('title',)}
    list_editable=['category','is_banner']
    search_fields=['title','slug']
    list_filter=['category','created_at']

    def show_image(self,obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="80"/>')
        else:
            return 'No Image'