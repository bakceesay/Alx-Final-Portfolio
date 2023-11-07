from django.conf.urls import include, url
from django.contrib import admin
from .views import * 


urlpatterns = [

#FixAsset
	url(r'^employee_list/$', employee_list, name='employee_list'),
	url(r'^employee_retire_list/$', employee_retire_list, name='employee_retire_list'),
	url(r'^employee/create/$', employee_create, name='employee_create'),
	url(r'^employee/(?P<id>\d+)/$', employee_edit, name='employee_edit'),
	url(r'^employee_import/$', employee_import, name='employee_import'),
	
	# url(r'^employee_promotion_list/$', employee_promotion_list, name='employee_promotion_list'),
	url(r'^employee_promotion/(?P<id>\d+)/$', employee_promotion, name='employee_promotion'),
	url(r'^employee_status_list/$', employee_status_list, name='employee_status_list'),
	url(r'^employee_promotion_list/$', employee_promotion_list, name='employee_promotion_list'),
	url(r'^employee_promotion_audit_list/$', employee_promotion_audit_list, name='employee_promotion_audit_list'),
	url(r'^employee_vocation_list/$', employee_vocation_list, name='employee_vocation_list'),
	url(r'^employee_history_list/$', employee_history_list, name='employee_history_list'),
	url(r'^employee_status/(?P<id>\d+)/$', employee_status, name='employee_status'),
	url(r'^employee_vocation/(?P<id>\d+)/$', employee_vocation, name='employee_vocation'),
	url(r'^employee_detail/(?P<id>\d+)/detail$', employee_detail, name='employee_detail'), #list items

	
	url(r'^employee/report/$', employee_report, name='employee_report'), #Report

	url(r'^settings/$', settings, name='settings'),
	# url(r'^fixassetsettings/$', fixassetsettings, name='fixassetsettings'),
]
