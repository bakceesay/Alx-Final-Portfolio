from django import forms
from .models import * 


import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

cannotBeEmpty = 'This field cannot be Empty'


##################################************************###############################

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['passport_picture',
					'employment_number',
					'title',
					'name',
					'gender',
					'marital_status',
					'tin_number',
					'School_of_graduation',
					'graduation_year',
					'highest_qualification',
					'email_address',
					'nationality',
					'home_country',
					'residence',
					'contact_number',
					'status',
					'dob',
					'place_of_birth',
					'qualification',
					'fad',
					'cad',
					'cd',
					'designation',
					'budget_entity',
					'unit',
					'division',
					'grade',
					'grade_point',
					'next_of_kin',
					]


	def clean_employment_number(self):
		employment_number = self.cleaned_data.get('employment_number')
		if (employment_number == ''):
			raise forms.ValidationError(cannotBeEmpty)
		for instance in Employee.objects.all():
			if instance.employment_number == employment_number:
				raise forms.ValidationError( str(employment_number) + ' is already assigned')
		return employment_number

	def clean_budget_entity(self):
		budget_entity = self.cleaned_data.get('budget_entity')
		if (budget_entity == None):
			raise forms.ValidationError(cannotBeEmpty)
		return budget_entity

	def clean_dob(self):
		dob = self.cleaned_data.get('dob')
		if (dob == None):
			raise forms.ValidationError(cannotBeEmpty)
		return dob

	def clean_fad(self):
		fad = self.cleaned_data.get('fad')
		if (fad == None):
			raise forms.ValidationError(cannotBeEmpty)
		return fad




class EmployeeEditForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['passport_picture',
					'employment_number',
					'title',
					'name',
					'gender',
					'marital_status',
					'tin_number',
					'School_of_graduation',
					'graduation_year',
					'highest_qualification',
					'email_address',
					'nationality',
					'home_country',
					'residence',
					'contact_number',
					'status',
					'dob',
					'place_of_birth',
					'qualification',
					'fad',
					'cad',
					'cd',
					'designation',
					'budget_entity',
					'unit',
					'division',
					'grade',
					'grade_point',
					'next_of_kin',
					]


	# def clean_employment_number(self):
	# 	employment_number = self.cleaned_data.get('employment_number')
	# 	if (employment_number == ''):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	for instance in Employee.objects.all():
	# 		if instance.employment_number == employment_number:
	# 			raise forms.ValidationError( str(employment_number) + ' is already assigned')
	# 	return employment_number

	def clean_budget_entity(self):
		budget_entity = self.cleaned_data.get('budget_entity')
		if (budget_entity == None):
			raise forms.ValidationError(cannotBeEmpty)
		return budget_entity

	def clean_dob(self):
		dob = self.cleaned_data.get('dob')
		if (dob == None):
			raise forms.ValidationError(cannotBeEmpty)
		return dob

	def clean_fad(self):
		fad = self.cleaned_data.get('fad')
		if (fad == None):
			raise forms.ValidationError(cannotBeEmpty)
		return fad




class EmployeePromotionForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [	'designation',
					'grade',
					'cad',
					]


	def clean_cad(self):
		cad = self.cleaned_data.get('cad')
		if (cad == None):
			raise forms.ValidationError(cannotBeEmpty)
		return cad


class EmployeePromotionSearchForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [	'employment_number',
					'name',
					'grade',
					'budget_entity',
					]



class EmployeeStatusForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [	'status',
					'status_start_date',
					'status_end_date',
					'alert_days',
					]

	def clean_status_start_date(self):
		status_start_date = self.cleaned_data.get('status_start_date')
		status = self.cleaned_data.get('status')
		if (status == 'Secondment') or (status == 'secondment') & (status_start_date == None):
			raise forms.ValidationError('Please specify the start date of secondment')
		return status_start_date

	def clean_status_end_date(self):
		status_end_date = self.cleaned_data.get('status_end_date')
		status = self.cleaned_data.get('status')
		if (status == 'Secondment') or (status == 'secondment') & (status_end_date == None):
			raise forms.ValidationError('Please specify the end date of secondment')
		return status_end_date



class EmployeeStatusSearchForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [	'employment_number',
					'vocation_start_date',
					'vocation_end_date',
					'vocation',
					'budget_entity',
					]

class EmployeeVocationForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [	'vocation',
					'vocation_start_date',
					'vocation_end_date',
					'alert_days',
					]

	def clean_vocation_start_date(self):
		vocation_start_date = self.cleaned_data.get('vocation_start_date')
		if (vocation_start_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		return vocation_start_date

	def clean_vocation_end_date(self):
		vocation_end_date = self.cleaned_data.get('vocation_end_date')
		if (vocation_end_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		return vocation_end_date



class EmployeeVocationSearchForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [	'employment_number',
					'vocation',
					'vocation_start_date',
					'vocation_end_date',
					'budget_entity',
					]




class EmployeeHistorySearchForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = [	'employment_number',
					'last_updated_from',
					'last_updated_to',
					'budget_entity',
					]


class CreateBudgetEntityForm(forms.ModelForm):
	class Meta:
		model = BudgetEntity
		fields = ['budget_entity']

	def clean_budget_entity(self):
		budget_entity = self.cleaned_data.get('budget_entity')
		if (budget_entity == ''):
			raise forms.ValidationError(cannotBeEmpty)
		for instance in BudgetEntity.objects.all():
			if budget_entity == instance.budget_entity:
				raise forms.ValidationError(str(instance.budget_entity) + ' is already created')
		return budget_entity




class CreateVocationForm(forms.ModelForm):
	class Meta:
		model = Vocation
		fields = ['vocation']

	def clean_vocation(self):
		vocation = self.cleaned_data.get('vocation')
		if (vocation == ''):
			raise forms.ValidationError(cannotBeEmpty)
		for instance in Vocation.objects.all():
			if vocation == instance.vocation:
				raise forms.ValidationError(str(instance.vocation) + ' is already created')
		return vocation



# class CreateDepartmentForm(forms.ModelForm):
# 	class Meta:
# 		model = Department
# 		fields = ['department']

# 	def clean_department(self):
# 		department = self.cleaned_data.get('department')
# 		if (department == ''):
# 			raise forms.ValidationError(cannotBeEmpty)
# 		for instance in Department.objects.all():
# 			if department == instance.department:
# 				raise forms.ValidationError(str(instance.department) + ' is already created')
# 		return department


class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['employment_number',
				'name',
				'gender',
				'budget_entity',
				'status',
				'export_to_CSV',
				]
