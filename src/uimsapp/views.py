from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect # HttpResponse allows the get_absolute_url to work ## and HttpresponseRedirect redirects page after a process
from django.contrib import messages
from datetime import date
from datetime import datetime # Import for date conversion in treasury report view
import datetime

import operator
from django.db.models import Q

import smtplib
import os # for Video Files
# from django.utils import timezone
import csv, socket
# import io 

# with io.TextIOWrapper(request.FILES["csv_file"].chunks(), encoding="utf-8") as text_file:
#     reader = csv.reader(text_file)


host = socket.gethostname()
# print host
# if (host == 'arbThinkPad' or host == 'nagiosserver'):

from .forms import *
from .models import *

from uimsproject.settings import BASE_DIR
from django.contrib.admin.models import LogEntry, ADDITION
from .resources import EmployeeResource, PersonResource # for import export app
from tablib import Dataset  # for import export app

from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
   """Requires user membership in at least one of the groups passed in."""

   def in_groups(u):
       if u.is_authenticated():
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)




@group_required('admins', 'seller')
def employee_list(request):
 #   	loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'SEARCH EMPLOYEES'
	headdashboard = 'DASHBOARD'

	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = Employee.objects.all().order_by('-last_updated')
		form = ReportForm(request.POST or None)
		title = ""
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'

		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"headdashboard": headdashboard,
		"assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = Employee.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), 
																				name__icontains=form['name'].value(), 
																				status__icontains=form['status'].value(),#.exclude(obsolete=True).exclude(auctioned=True)
																				gender__icontains=form['gender'].value())#.exclude(obsolete=True).exclude(auctioned=True)
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			"assetCount": Count,
			}
			if form['export_to_CSV'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
				writer = csv.writer(response)
				writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
				instance = queryset
				for row in instance:
					writer.writerow([row.employment_number, row.name, row.grade, row.fad])
				return response
	return render(request, "employee_list.html", context)



@group_required('admins', 'seller')
def employee_retire_list(request):
 #   	loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'SEARCH EMPLOYEES'
	headdashboard = 'DASHBOARD'

	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = Employee.objects.all().order_by('-last_updated').filter(dob__lte="1961-01-01")
		form = ReportForm(request.POST or None)
		title = ""
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'

		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"headdashboard": headdashboard,
		"assetCount": Count,
		}
		
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
			writer = csv.writer(response)
			writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
			instance = queryset
			for row in instance:
				writer.writerow([row.employment_number, row.name, row.grade, row.fad])
			return response
	return render(request, "employee_retire_list.html", context)





def employee_create(request):
	form = EmployeeForm(request.POST or None, request.FILES or None)
	submit = "Create"
	headdashboard = 'DASHBOARD'

	if form.is_valid():
		instance = form.save(commit=False)
		dob = instance.dob
		retirement = dob.replace(year=dob.year+60)
		# retirement.year
		instance.date_of_retirement = dob.replace(year=dob.year+60)
	 	instance.added_by = str(request.user)
		instance.save()
		message = str(instance.employment_number) + " Successfully Added"
		messages.success(request, message)
		return redirect("uimsapp:employee_create")
	context = {
		"form": form,
		"headdashboard": headdashboard,
		"title": "NEW ENTRY",
		"submit": submit,
		"username": 'Created By: ' + str(request.user),
	}
	return render(request, "employeentry.html", context)


def employee_detail(request, id=None):    
    instance = get_object_or_404(Employee, id=id)
    querysetEmployee = Employee.objects.all().filter(id=instance.id)
    headdashboard = 'DASHBOARD'
    # querysetLeave = leave.objects.all().filter(
    #                                             employee_name_id=instance.id,
    #                                             approval='Approved'
    #                                             ).order_by('balance')

    # request.user = request.user
    # form = ProfileDetailForm(request.POST or None, instance=instance)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.save()
    #     return redirect('/profile/profile_list')
    context = {
            "title": 'Edit ' + str(instance.name),
            "headdashboard": headdashboard,
            "user": request.user,
            "querysetProfile": querysetEmployee,

        }
    return render(request, "employee_detail.html", context)



def employee_edit(request, id=None):
	signin = 'Sign in here'
	instance = get_object_or_404(Employee, id=id)
	form = EmployeeEditForm(request.POST or None, request.FILES or None, instance=instance)

	submit = "Save Changes"
	# today = date.today()
	# yearsPast = ((today - instance.dcd).days)/365
	# count = 1
	# while (count <= yearsPast):
		
	# 	dpy = instance.cost/instance.eul
	# 	cda = instance.cost - dpy
	# 	instance.nbv = cda
	# 	print 'Year ' + str(count) + ' depreciation = ' + str(dpy)
	# 	print 'Year ' + str(count) + ' net book value = ' + str(instance.nbv) 

	# 	count += 1
	
	if form.is_valid():
		instance = form.save(commit=False)
	 	instance.added_by = str(request.user)
	 	instance.updated_by = str(request.user)
		instance.save()
		messages.success(request, str(instance.employment_number) + " Successfully Saved.")

		return redirect("uimsapp:employee_list")
	context = {
			"login": signin,
			"title": str(instance.employment_number),
			"instance": instance,
			"form": form,
			"submit": submit,
			"username": 'Updated By: ' + str(request.user),
		}
	return render(request, "edit.html", context)


# def employee_promotion(request, id=None):
# 	signin = 'Sign in here'
# 	instance = get_object_or_404(Employee, id=id)
# 	form = EmployeePromotionForm(request.POST or None, request.FILES or None, instance=instance)
# 	submit = "Save Changes"
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 	 	instance.updated_by = str(request.user)
# 		instance.save()
# 		messages.success(request, str(instance.employment_number) + " Successfully Saved.")
# 		return redirect("uimsapp:employee_list")
# 	context = {
# 			"login": signin,
# 			"title": str(instance.employment_number),
# 			"instance": instance,
# 			"form": form,
# 			"submit": submit,
# 			"username": 'Updated By: ' + str(request.user),
# 		}
# 	return render(request, "edit.html", context)



def employee_status(request, id=None):
	signin = 'Sign in here'
	instance = get_object_or_404(Employee, id=id)
	form = EmployeeStatusForm(request.POST or None, request.FILES or None, instance=instance)
	submit = "Save Changes"
	if form.is_valid():
		instance = form.save(commit=False)
	 	instance.updated_by = str(request.user)
		instance.save()
		messages.success(request, str(instance.employment_number) + " Successfully Saved.")
		return redirect("uimsapp:employee_status_list")
	context = {
			"login": signin,
			"title": str(instance.employment_number),
			"instance": instance,
			"form": form,
			"submit": submit,
			"username": 'Updated By: ' + str(request.user),
		}
	return render(request, "edit.html", context)





def employee_status_list(request):
 #   	loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'STATUS OF EMPLOYEES'
	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = Employee.objects.all().order_by('-last_updated')
		form = EmployeeStatusSearchForm(request.POST or None)
		title = ""
		today = date.today()
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'
		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"today": today,
		"assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = Employee.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), status__icontains=form['status'].value())#.exclude(obsolete=True).exclude(auctioned=True)
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			"assetCount": Count,
			# "status_days_left": status_days_left,
			"today": today,


			}
			# if form['export_to_CSV'].value() == True:
			# 	response = HttpResponse(content_type='text/csv')
			# 	response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
			# 	writer = csv.writer(response)
			# 	writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
			# 	instance = queryset
			# 	for row in instance:
			# 		writer.writerow([row.employment_number, row.name, row.grade, row.fad])
			# 	return response
	return render(request, "status.html", context)




########## PROMOTION


def employee_promotion(request, id=None):
	signin = 'Sign in here'
	instance = get_object_or_404(Employee, id=id)
	form = EmployeePromotionForm(request.POST or None, request.FILES or None, instance=instance)
	submit = "Save Changes"
	if form.is_valid():
		instance = form.save(commit=False)
	 	instance.updated_by = str(request.user)
		instance.save()
		messages.success(request, str(instance.employment_number) + " Successfully Saved.")
		return redirect("uimsapp:employee_promotion_list")
	context = {
			"login": signin,
			"title": str(instance.employment_number),
			"instance": instance,
			"form": form,
			"submit": submit,
			"username": 'Updated By: ' + str(request.user),
		}
	return render(request, "edit.html", context)





def employee_promotion_list(request):
 	# loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'EMPLOYEE PROMOTION'
	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = Employee.objects.all().order_by('-last_updated')
		form = EmployeePromotionSearchForm(request.POST or None)
		title = ""
		today = date.today()
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'
		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"today": today,
		"assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = Employee.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), name__icontains=form['name'].value(), grade__icontains=form['grade'].value())#.exclude(obsolete=True).exclude(auctioned=True)
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			"assetCount": Count,
			# "status_days_left": status_days_left,
			"today": today,


			}
			# if form['export_to_CSV'].value() == True:
			# 	response = HttpResponse(content_type='text/csv')
			# 	response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
			# 	writer = csv.writer(response)
			# 	writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
			# 	instance = queryset
			# 	for row in instance:
			# 		writer.writerow([row.employment_number, row.name, row.grade, row.fad])
			# 	return response
	return render(request, "promotion.html", context)



def employee_promotion_audit_list(request):
 	# loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'EMPLOYEE PROMOTION HISTORY'
	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = EmployeeAudit.objects.all().order_by('-last_updated')
		form = EmployeePromotionSearchForm(request.POST or None)
		title = ""
		today = date.today()
		if len(queryset) == 1:
			Count = '1 Listed'
		else:
			Count = str(len(queryset)) + ' Listed'
		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"today": today,
		# "assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = EmployeeAudit.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), name__icontains=form['name'].value(), grade__icontains=form['grade'].value())#.exclude(obsolete=True).exclude(auctioned=True)
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			# "assetCount": Count,
			# "status_days_left": status_days_left,
			"today": today,


			}
			# if form['export_to_CSV'].value() == True:
			# 	response = HttpResponse(content_type='text/csv')
			# 	response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
			# 	writer = csv.writer(response)
			# 	writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
			# 	instance = queryset
			# 	for row in instance:
			# 		writer.writerow([row.employment_number, row.name, row.grade, row.fad])
			# 	return response
	return render(request, "promotion_audit.html", context)


########## END PROMOTION



########## VOCATION


def employee_vocation(request, id=None):
	signin = 'Sign in here'
	instance = get_object_or_404(Employee, id=id)
	form = EmployeeVocationForm(request.POST or None, request.FILES or None, instance=instance)
	submit = "Save Changes"
	if form.is_valid():
		instance = form.save(commit=False)
	 	instance.updated_by = str(request.user)
		instance.save()
		messages.success(request, str(instance.employment_number) + " Successfully Saved.")
		return redirect("uimsapp:employee_vocation_list")
	context = {
			"login": signin,
			"title": str(instance.employment_number),
			"instance": instance,
			"form": form,
			"submit": submit,
			"username": 'Updated By: ' + str(request.user),
		}
	return render(request, "edit.html", context)





def employee_vocation_list(request):
 #   	loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'EMPLOYEE VOCATION'
	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = Employee.objects.all().order_by('-last_updated')
		form = EmployeeVocationSearchForm(request.POST or None)
		title = ""
		today = date.today()
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'
		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"today": today,
		"assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = Employee.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), status__icontains=form['status'].value())#.exclude(obsolete=True).exclude(auctioned=True)
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			"assetCount": Count,
			# "status_days_left": status_days_left,
			"today": today,


			}
			# if form['export_to_CSV'].value() == True:
			# 	response = HttpResponse(content_type='text/csv')
			# 	response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
			# 	writer = csv.writer(response)
			# 	writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
			# 	instance = queryset
			# 	for row in instance:
			# 		writer.writerow([row.employment_number, row.name, row.grade, row.fad])
			# 	return response
	return render(request, "vocation_list.html", context)




def employee_history_list(request):
 #   	loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'EMPLOYEE HISTORY'
	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = EmployeeAudit.objects.all().order_by('-last_updated')
		form = EmployeeHistorySearchForm(request.POST or None)
		title = ""
		today = date.today()
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'
		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"today": today,
		"assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = EmployeeAudit.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), )#.exclude(obsolete=True).exclude(auctioned=True)
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			"assetCount": Count,
			# "status_days_left": status_days_left,
			"today": today,


			}
			# if form['export_to_CSV'].value() == True:
			# 	response = HttpResponse(content_type='text/csv')
			# 	response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
			# 	writer = csv.writer(response)
			# 	writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
			# 	instance = queryset
			# 	for row in instance:
			# 		writer.writerow([row.employment_number, row.name, row.grade, row.fad])
			# 	return response
	return render(request, "history_list.html", context)






def employee_report(request):
 #   	loginfirst = 'Sorry... You have to login before you can access this page.'
	# signin = 'Sign in here'
	heading = 'OTHER REPORTS'
	context = {
		# "signin": signin,
		# "title": loginfirst,
	}
	if request.user.is_authenticated():
		queryset = Employee.objects.all().order_by('-last_updated')
		form = ReportForm(request.POST or None)
		title = ""
		today = date.today()
		if len(queryset) == 1:
			Count = '1 Employee Listed'
		else:
			Count = str(len(queryset)) + ' Employees Listed'
		context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		"heading": heading,
		"today": today,
		"assetCount": Count,
		}
		if request.method == 'POST':
			budget_entity = form['budget_entity'].value()
			# department = form['department'].value()
			querysetAll = Employee.objects.all().order_by('-last_updated').filter(employment_number__icontains=form['employment_number'].value(), 
																					gender__icontains=form['gender'].value(), 
																					status__icontains=form['status'].value(), 
																					name__icontains=form['name'].value())
			if (budget_entity != ''):
				queryset = querysetAll.filter(budget_entity_id=budget_entity)

			if (budget_entity == ''):
				queryset = querysetAll

			# if (budget_entity != '' and department == ''):
			# 	queryset = querysetAll.filter(budget_entity_id=budget_entity)

			# if (budget_entity == '' and department != ''):
			# 	queryset = querysetAll.filter(department_id=department)

			if len(queryset) == 1:
				Count = '1 Employee Listed'
			else:
				Count = str(len(queryset)) + ' Employees Listed'

			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			"heading": heading,
			"assetCount": Count,
			"today": today,


			}
			if form['export_to_CSV'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename="Employee.csv"'
				writer = csv.writer(response)
				writer.writerow(['EMP NUMBER', 'NAME', 'GRADE', 'FIRST APPOINTMENT DATE'])
				instance = queryset
				for row in instance:
					writer.writerow([row.employment_number, row.name, row.grade, row.fad])
				return response
	return render(request, "employee_report.html", context)






########## END VOCATION
# with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
#        reader = csv.reader(text_file, delimiter=';')                
#        for row in reader:

def employee_import(request):
    if request.method == 'POST':
        # person_resource = EmployeeResource()
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'import_employee.html')


def frontadmin(request):
	print str(request.user)
	title = 'ADMIN SITE'
	context = {
		"title": title,
	}
	if request.user.is_authenticated():
		print str(request.user)
		# title = "Welcome %s" %(request.user)
		title = (request.user)
		context = {
			"title": title,
		}


	return render(request, "frontadmin.html",context)


def home(request):
	print str(request.user)
	title = 'FOR AUTHORIZED PERSONELS ONLY'
	context = {
		"title": title,
	}
	if request.user.is_authenticated():
		print str(request.user)
		title = (request.user)
		context = {
			"title": title,
		}


	return render(request, "base.html",context)


	########################### Home View + Login Form Starts Here #########################
def login(request):
	print str(request.user)
	title = 'Welcome'
	context = {
	"title": title,
	}
	if request.user.is_authenticated():
		print str(request.user)
		title = "Welcome %s" %(request.user)
		loginform = LoginForm(request.POST or None)
		context = {
			"title": title,
			"loginform": loginform
		}



	return render(request, "login.html",context)





##################################### End of Home View + Login Form View ###################################




def settings(request):
	print str(request.user)
	loginfirst = 'Sorry... You have to login before you can access this page.'
	signin = 'Sign in here'
	context = {
		"title": loginfirst,
		"signin": signin,
	}
	if request.user.is_authenticated():
		FormBudgetEntity = CreateBudgetEntityForm(request.POST or None)
		FormVocation = CreateVocationForm(request.POST or None)
		submit = "Create"
		if FormBudgetEntity.is_valid():
			instance = FormBudgetEntity.save(commit=False)
			instance.save()
			message = str(instance.budget_entity) + " Successfully Created"
			messages.success(request, message)
			return redirect("uimsapp:settings")

		elif FormVocation.is_valid():
			instance = FormVocation.save(commit=False)
			instance.save()
			message = str(instance.vocation) + " Successfully Created"
			messages.success(request, message)
			return redirect("uimsapp:settings")
		context = {
			"BudgetEntityForm": FormBudgetEntity,
			"VocationForm": FormVocation,
			"title": "SETTINGS",
			"submit": submit,
			"username": 'Created By: ' + str(request.user),
		}
	return render(request, "settings.html", context)






def custom_404(request):
	print str(request.user)
	return render(request, "404.html")

def custom_500(request):
	print str(request.user)
	return render_to_response('500.html', RequestContex(request))
