from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from simple_history.admin import SimpleHistoryAdmin

from .forms import *
from .models import *


################FixAsset
class EmployeeAdmin(admin.ModelAdmin):
 	list_display = ['employment_number', 'name']
 	form = EmployeeForm # This is the Form imported above "from .forms"
 	list_filter = ['employment_number']
 	search_fields = ['employment_number', 'name']




class BudgetEntityAdmin(admin.ModelAdmin):
 	list_display = ["budget_entity"]
 	form = CreateBudgetEntityForm
 	list_filter = ['budget_entity']
 	search_fields = ['budget_entity']



# class DepartmentAdmin(admin.ModelAdmin):
#  	list_display = ["department"]
#  	form = CreateDepartmentForm
#  	list_filter = ['department']
#  	search_fields = ['department']




admin.site.register(Person)
admin.site.register(Employee, EmployeeAdmin)

admin.site.register(BudgetEntity, BudgetEntityAdmin)
# admin.site.register(Department, DepartmentAdmin)