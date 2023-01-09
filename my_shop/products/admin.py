from django.contrib import admin
from .models import Product


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)


admin.site.register(Product)


class MyModelAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/my_own_admin.js',)
        css = {
             'all': ('css/admin/my_own_admin.css',)
        }




# Register your models here.


