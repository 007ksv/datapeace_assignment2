from django.contrib import admin
from .models import CustomUser

# registering our model to admin pannel

admin.site.register(CustomUser)

