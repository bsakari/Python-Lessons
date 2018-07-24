from peewee import *
from os import path

ROOT = path.dirname(path.realpath(__file__))

db = SqliteDatabase(path.join(ROOT,"persons.db"))

class Person(Model):
    name = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    password = CharField()
    class Meta:
        database = db

Person.create_table(fail_silently=True)
Person.create(name = "Dan",email = "dcjcijnsjuuu@gmail.com",age = 48,password = "dan123")
Person.create(name = "Brio",email = "brcsjcughoooooos@gmail.com",age = 40,password = "brio123")
user1 = Person.get(id=1)
print(user1.name,user1.email,user1.age,user1.password)
