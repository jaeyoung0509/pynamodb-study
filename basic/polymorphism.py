"""
PynamoDB supports polymorphism through the use of discriminators.

A discriminator is a value that is written to DynamoDB that identifies the python class being stored.
"""
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, DiscriminatorAttribute

class ParentModel(Model):
    class Meta:
        table_name = 'polymorphic_table'
    id = UnicodeAttribute(hash_key=True)
    cls = DiscriminatorAttribute()

class FooModel(ParentModel, discriminator='Foo'):
    foo = UnicodeAttribute()

class BarModel(ParentModel, discriminator='Bar'):
    bar = UnicodeAttribute()

BarModel(id='Hello', bar='World!').serialize()