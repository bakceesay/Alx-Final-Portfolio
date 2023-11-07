from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime, date 
# from simple_history.models import HistoricalRecords


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    

class BudgetEntity(models.Model):
	budget_entity = models.CharField(max_length=200, default='', blank=True, null=True)
	
	positionNameOne = models.CharField('Position One Name', max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField('Grade', max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField('Quantity', blank=True, null=True)
	ocupiedOne = models.IntegerField('Quantiry Occupied', blank=True, null=True)
	vacantOne = models.IntegerField('Quantity Vacant', blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)

	positionNameOne = models.CharField(max_length=120, default='', blank=True, null=True)
	gradeOne = models.CharField(max_length=120, default='', blank=True, null=True)
	quantityOne = models.IntegerField(blank=True, null=True)
	ocupiedOne = models.IntegerField(blank=True, null=True)
	vacantOne = models.IntegerField(blank=True, null=True)
	def __unicode__(self):
		return self.budget_entity


class Vocation(models.Model):
	vocation = models.CharField(max_length=200, default='', blank=True, null=True)
	def __unicode__(self):
		return self.vocation


# ##### NEW FIX ASSET 


def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.employment_number, instance.employment_number, extension)






class Employee(models.Model):
	passport_picture = models.FileField(upload_to=upload_location, null=True, blank=True)
	employment_number = models.CharField(max_length=120, default='', blank=True, null=True)# 7 digiits and numbers only
	title = models.CharField(max_length=120, default='', blank=True, null=True)
	name = models.CharField(max_length=120, default='', blank=True, null=True)
	nationality = models.CharField(max_length=120, default='', blank=True, null=True)
	id_card_number = models.CharField(max_length=120, default='', blank=True, null=True)
	home_country = models.CharField(max_length=120, default='', blank=True, null=True)
	residence = models.CharField(max_length=120, default='', blank=True, null=True)
	contact_number = models.CharField(max_length=120, default='', blank=True, null=True)
	email_address = models.CharField(max_length=120, default='', blank=True, null=True)
	status = models.CharField(max_length=120, default='', blank=True, null=True)
	status_start_date= models.DateField('Status Start Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	status_end_date= models.DateField('Status End Date', auto_now_add=False, auto_now=False, blank=True, null=True)

	# vocation = models.CharField(max_length=120, default='', blank=True, null=True)
	vocation = models.ForeignKey(Vocation, blank=True, null=True)
	vocation_start_date= models.DateField('Vocation Start Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	vocation_end_date= models.DateField('Vocation End Date', auto_now_add=False, auto_now=False, blank=True, null=True)

	# status_alert_date= models.DateField('Alert Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	alert_days = models.IntegerField('Alert when status due in Days', blank=True, null=True)
	dob = models.DateField('Date of Birth', auto_now_add=False, auto_now=False, blank=True, null=True)
	place_of_birth = models.CharField(max_length=120, default='', blank=True, null=True)
	fad= models.DateField('First Appointment Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	cad= models.DateField('Current Appointment Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	cad= models.DateField('Current Appointment Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	cd= models.DateField('Confirmed Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	graduation_year= models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	designation = models.CharField(max_length=120, default='', blank=True, null=True)
	budget_entity = models.ForeignKey(BudgetEntity, blank=True, null=True)

	division_choice = (
		('Greater Banjul', 'Greater Banjul'),
		('West coast Region', 'West coast Region'),
		('North Bank Region', 'North Bank Region'),
		('Lower River Region', 'North Bank Region'),
		('Central River Region', 'Central River Region'),
		('Upper River Region', 'Central River Region'),
		)
	division = models.CharField('Region', max_length=50, blank=True, null=True, choices=division_choice)

	duty_station = models.CharField(max_length=120, default='', blank=True, null=True)
	grade = models.IntegerField(blank=True, null=True)
	grade_point = models.IntegerField(blank=True, null=True)
	next_of_kin = models.CharField(max_length=120, default='', blank=True, null=True)
	qualification = models.TextField('Educational Background', max_length=300, default='', blank=True, null=True)
	tin_number = models.CharField(max_length=120, default='', blank=True, null=True)
	added_by = models.CharField(max_length=120, default='', blank=True, null=True)
	updated_by = models.CharField(max_length=120, default='', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	date_of_retirement = models.CharField(max_length=30, blank=True, null=True) 
	School_of_graduation = models.CharField(max_length=30, blank=True, null=True) 
	marital_status_choice= (
		('Married', 'Married'),
		('Single', 'Single'),
		)
	marital_status = models.CharField(max_length=30, blank=True, null=True, choices=marital_status_choice)
	unit_choice= (
		('Human resource', 'Human resource'),
		('Accounts', 'Accounts'),
		('Administration', 'Administration'),
		('Communication', 'Communication'),
		('Records', 'Records'),
		('Stores', 'Stores'),
		('Support staff', 'Support staff'),
		)
	unit = models.CharField(max_length=30, blank=True, null=True, choices=unit_choice)

	gender_choice = (
		('Male', 'Male'),
		('Female', 'Female'),
		)
	gender = models.CharField(max_length=30, blank=True, null=True, choices=gender_choice)
	highest_qualification = (
		('None', 'None'),
		('Arabic', 'Arabic'),
		('Primary School', 'Primary School'),
		('Upper Basic', 'Upper Basic'),
		('Senior Secondary School', 'Senior Secondary School'),
		('CAT', 'CAT'),
		('AAT', 'AAT'),
		('ACCA', 'ACCA'),
		('ECD', 'ECD'),
		('PTC', 'PTC'),
		('HTC', 'HTC'),
		('Other Professional Qualification', 'Other Professional Qualification'),
		('Bachelors Degree', 'Bachelors Degree'),
		('Bachelors/Masters Degree', 'Bachelors/Massters Degree'),
		('Bachelors Degree/ACCA', 'Bachelors Degree/ACCA'),
		('Masters Degree', 'Masters Degree'),
		('Masters Degree/ACCA', 'Masters Degree/ACCA'),
		('Bachelors/Masters Degree/ACCA', 'Bachelors/Masters Degree/ACCA'),
		('Professional/Bachelors Degree', 'Professional/Bachelors Degree'),
		('Professional/Masters Degree', 'Professional/Masters Degree'),
		('Professional/Bachelors/Masters Degree', 'Professional/Bachelors/Masters Degree'),
		)
	highest_qualification = models.CharField(max_length=50, blank=True, null=True, choices=highest_qualification)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	@property
	def age_in_days(self):
		today = date.today()
		result = self.status_end_date - today
		return result.days

	class Meta:
		managed = True
		db_table = 'uimsapp_employee'

	# def ends_within_7_days(self):
	# 	return (date.today() - self.status_end_date).days <= 7

	def get_absolute_url(self):
		return reverse("uimsapp:employee_edit", kwargs={"id": self.id})

	def get_absolute_promotion_url(self):
		return reverse("uimsapp:employee_promotion", kwargs={"id": self.id})

	def get_absolute_status_url(self):
		return reverse("uimsapp:employee_status", kwargs={"id": self.id})

	def get_absolute_vocation_url(self):
		return reverse("uimsapp:employee_vocation", kwargs={"id": self.id})

	def get_absolute_emp_Details_url(self):
		return reverse("uimsapp:employee_detail", kwargs={"id": self.id})

	# def get_absolute_change_user_url(self):
	# 	return reverse("uimsapp:employment_list_change_user_edit", kwargs={"id": self.id})

	# def get_absolute_auction_url(self):
	# 	return reverse("uimsapp:employment_list_auction_edit", kwargs={"id": self.id})

	# def get_absolute_url_more_trails(self):
	# 	return reverse("uimsapp:employment_list_more_trails", kwargs={"id": self.id})

	def __unicode__(self):
		return self.employment_number







class EmployeeAudit(models.Model):
	passport_picture = models.FileField(upload_to=upload_location, null=True, blank=True)
	employment_number = models.CharField(max_length=120, default='', blank=True, null=True)# 7 digiits and numbers only
	title = models.CharField(max_length=120, default='', blank=True, null=True)
	name = models.CharField(max_length=120, default='', blank=True, null=True)
	gender = models.CharField(max_length=120, default='', blank=True, null=True)
	nationality = models.CharField(max_length=120, default='', blank=True, null=True)
	id_card_number = models.CharField(max_length=120, default='', blank=True, null=True)
	home_country = models.CharField(max_length=120, default='', blank=True, null=True)
	residence = models.CharField(max_length=120, default='', blank=True, null=True)
	contact_number = models.CharField(max_length=120, default='', blank=True, null=True)
	email_address = models.CharField(max_length=120, default='', blank=True, null=True)
	status = models.CharField(max_length=120, default='', blank=True, null=True)
	status_start_date= models.DateField('Status Start Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	status_end_date= models.DateField('Status End Date', auto_now_add=False, auto_now=False, blank=True, null=True)

	# vocation = models.CharField(max_length=120, default='', blank=True, null=True)
	vocation = models.ForeignKey(Vocation, blank=True, null=True)
	vocation_start_date= models.DateField('Vocation Start Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	vocation_end_date= models.DateField('Vocation End Date', auto_now_add=False, auto_now=False, blank=True, null=True)

	# status_alert_date= models.DateField('Alert Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	alert_days = models.IntegerField('Alert when status due in Days', blank=True, null=True)
	dob = models.DateField('Date of Birth', auto_now_add=False, auto_now=False, blank=True, null=True)
	place_of_birth = models.CharField(max_length=120, default='', blank=True, null=True)
	fad= models.DateField('First Appointment Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	cad= models.DateField('Current Appointment Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	cd= models.DateField('Confirmed Date', auto_now_add=False, auto_now=False, blank=True, null=True)
	designation = models.CharField(max_length=120, default='', blank=True, null=True)
	budget_entity = models.ForeignKey(BudgetEntity, blank=True, null=True)
	division = models.CharField(max_length=120, default='', blank=True, null=True)
	duty_station = models.CharField(max_length=120, default='', blank=True, null=True)
	grade = models.IntegerField(blank=True, null=True)
	grade_point = models.IntegerField(blank=True, null=True)
	next_of_kin = models.CharField(max_length=120, default='', blank=True, null=True)
	qualification = models.TextField(max_length=3000, default='', blank=True, null=True)
	tin_number = models.CharField(max_length=120, default='', blank=True, null=True)
	marital_status = models.CharField(max_length=120, default='', blank=True, null=True)
	added_by = models.CharField(max_length=120, default='', blank=True, null=True)
	updated_by = models.CharField(max_length=120, default='', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	# class Meta:
	# 	managed = True
	# 	db_table = 'uimsapp_employeeaudit'


	def __unicode__(self):
		return self.employment_number



class Report(models.Model):
	employment_number = models.CharField(max_length=120, default='', blank=True, null=True)
	name = models.CharField(max_length=120, default='', blank=True, null=True)
	gender = models.CharField(max_length=120, default='', blank=True, null=True)
	budget_entity = models.ForeignKey(BudgetEntity, blank=True, null=True)
	status = models.CharField(max_length=120, default='', blank=True, null=True)
	start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	last_updated_from = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	last_updated_to = models.DateField("To" ,auto_now_add=False, auto_now=False, blank=True, null=True)
	export_to_CSV = models.BooleanField(default=False)