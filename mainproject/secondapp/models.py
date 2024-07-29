from django.db import models

class Information:
    img: str

# Creating a model to create table in database

# py manage.py makemigrations
# py manage.py sqlmigrate secondapp 0001 
# requires packagename migration code from migrations
# py manage.py migrate
class InformationModel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='updImg')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)