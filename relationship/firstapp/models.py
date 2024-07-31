from django.db import models

class Interest(models.Model):
    interest = models.CharField(max_length=50)

    def __str__(self):
        return self.interest

class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    is_student = models.BooleanField(default=False)
    interest = models.ManyToManyField(Interest)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    #This establishes a many-to-one relationship: many cities can be associated with one country.
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.person.name} belongs to {self.country}'
