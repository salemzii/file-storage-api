from django.contrib import admin
from .models import file_uploader, image


admin.site.register(file_uploader)
admin.site.register(image)

