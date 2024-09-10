from django.contrib import admin
from django.utils.html import format_html
from . models import Student, Category, Product

# Register your models here.
@admin.register(Student)
class StdAdmin(admin.ModelAdmin):
    list_display=['sname', 'smobile', 'saddress']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['cat_id','cat_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def prdImg(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    list_display=['name', 'description', 'price', 'category', 'prdImg']

