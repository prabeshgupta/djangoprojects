# Django Making Queries

# Start interactive shell to query database
py manage.py shell

# Syntax
variable = Model.objects.all()/get()/filter()/exclude()
print(variable)

# Add row to the table
from firstapp.models import City
a = City(city="Pachthar")
a.save()

# Retrieve rows from table 
a = City.objects.all()
print(a)

# Slicing
a = City.objects.all()[0:5]
print(a)

# Order by city name
a = City.objects.all().order_by('city')
b = Person.objects.all().order_by('-name')
print(a)
print(b)

# Get method using name and id
a = City.objects.get(city='Humla')
b = City.objects.get(id=4)
print(a,b)

# Retrieve rows that starts and ends with (Case sensitive)
a = City.objects.filter(city__startswith='Pa')
b = City.objects.filter(city__endswith='c')
print(a,b)

# Retrieve rows that starts and ends with (Case insensitive)
a = City.objects.filter(city__istartswith='r')
b = City.objects.filter(city__iendswith='c')
print(a,b)

# Check if row exist or not
a = City.objects.filter(city='Kathmandu').exists()
print(a)

a = City.objects.filter(city__exact='Dolpa')
b = City.objects.filter(city__iexact='bHaktaPur')
print(a)
print(b)

# Check rows containing certain thing
a = City.objects.filter(city__contains='Pur')
print(a)

# Working with multiple tables
from firstapp.models import *    
person =  Person.objects.get(id=1)
interests = person.interest.all()
print(interest)

# Exclude certain thing
a = City.objects.all().exclude(city='Bhaktapur')
b = City.objects.all().exclude(city__in=['Dolpa','Pokhara'])
print(a.order_by('city'))
print(b)