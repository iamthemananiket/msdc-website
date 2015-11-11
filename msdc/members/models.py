from mongoengine import *

# Create your models here.
class Member(Document):
    first_name = StringField(max_length = 100,required = True)
    last_name = StringField(max_length = 30,required = True)
    designation = StringField(default = "member")
    age = IntField(min_value = 10, max_value = 50)
    level = IntField(default = 1)
    #skills = ReferenceField()
