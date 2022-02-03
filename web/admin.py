from django.contrib import admin
from web.models import Option


class OptionAdmin(admin.ModelAdmin):
    list_display = ["id","logo","name"]

admin.site.register(Option,OptionAdmin)

