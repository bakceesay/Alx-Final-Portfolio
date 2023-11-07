from import_export import resources
from .models import Employee, Person

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person