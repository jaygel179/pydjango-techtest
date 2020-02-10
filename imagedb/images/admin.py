from django.contrib import admin
from .models import Image, ImageLabel


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageLabel)
class ImageLabelAdmin(admin.ModelAdmin):
    pass
