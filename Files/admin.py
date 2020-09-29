from django.contrib import admin
from .models import files
class filesAdmin(admin.ModelAdmin):
    list_display=['chapter','subject']
    search_fields=('chapter','subject')
admin.site.register(files,filesAdmin)