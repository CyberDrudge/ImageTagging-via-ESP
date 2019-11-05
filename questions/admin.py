from django.contrib import admin
from .models import PrimaryImage, Selected, SecondaryImage

# Register your models here.
admin.site.register(PrimaryImage)
admin.site.register(SecondaryImage)
admin.site.register(Selected)
