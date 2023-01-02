from pynamodb.models import Model
from pynamodb.attributes import MapAttribute, UnicodeAttribute, ListAttribute, VersionAttribute

class OfficeEmployeeMap(MapAttribute):
    office_employee_id = UnicodeAttribute()
    person = UnicodeAttribute()

    def __eq__(self, other):
        return isinstance(other, OfficeEmployeeMap) and self.person == other.person

    def __repr__(self):
        return str(vars(self))

class Office(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = 'office'
        host = ""
    office_id = UnicodeAttribute(hash_key=True)
    employees = ListAttribute(of=OfficeEmployeeMap)
    name = UnicodeAttribute()
    version = VersionAttribute()