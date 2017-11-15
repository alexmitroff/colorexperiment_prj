from django.contrib import admin
from experiment.models import *

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

class StimulAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        ]

admin.site.register(Stimul, StimulAdmin)    
admin.site.register(Answer)    
admin.site.register(UserInfo)
admin.site.register(ImageType)
