from pynamodb.attributes import Attribute
from pynamodb.constants import BINARY

class CustomAttribute(Attribute):
    """
    A custom model attribute
    """

    # This tells PynamoDB that the attribute is stored in DynamoDB as a binary
    # attribute
    attr_type = BINARY

    def serialize(self, value):
        # convert the value to binary and return it
        ...

    def deserialize(self, value):
        # convert the value from binary back into whatever type you require
        ...

import  pickle
from pynamodb.attributes import BinaryAttribute, UnicodeAttribute, MapAttribute, NumberAttribute, ListAttribute
from pynamodb.models import Model
class Color:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<Color: %s> {self.name}"

class PickleAttribute(BinaryAttribute):
    def serialize(self, value):
        return super(PickleAttribute, self).serialize(pickle.dumps(value))

    def deserialize(self, value):
        return pickle.loads(super(PickleAttribute, self).deserialize(value))

class CustomAttribute(Model):
    class Meta:
        ...
    id = UnicodeAttribute(hash_key=True)
    objc = PickleAttribute()


class OfficeEmployeeMap(MapAttribute):
    office_employee_id = NumberAttribute()
    person = UnicodeAttribute()


class Office(Model):
    class Meta:
        table_name = 'OfficeModel'
    office_id = NumberAttribute(hash_key=True)
    employees = ListAttribute(of=OfficeEmployeeMap)