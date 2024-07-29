from django.contrib import admin
from .models import InformationModel

#py manage.py createsuperuser

admin.site.register(InformationModel)
