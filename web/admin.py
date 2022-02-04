from django.contrib import admin
from web.models import Option,Help,Price


class OptionAdmin(admin.ModelAdmin):
    list_display = ["id","logo","name","is_active"]

admin.site.register(Option,OptionAdmin)


class HelpAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","description"]

admin.site.register(Help,HelpAdmin)


class PriceAdmin(admin.ModelAdmin):
    list_display = ["id","title"]

admin.site.register(Price,PriceAdmin)

