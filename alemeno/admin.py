from django.contrib import admin

from .models import Kid, Image

# Register your models here.
admin.site.register(Kid)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ("image_tag",)
