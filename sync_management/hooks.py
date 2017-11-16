# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sync_management"
app_title = "Sync Management"
app_publisher = "ERPX"
app_description = "Sync document from this server to another"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "erpx@mail.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sync_management/css/sync_management.css"
# app_include_js = "/assets/sync_management/js/sync_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/sync_management/css/sync_management.css"
# web_include_js = "/assets/sync_management/js/sync_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sync_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sync_management.install.before_install"
# after_install = "sync_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sync_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Item": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Customer": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Account": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"BOM": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Supplier": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Territory": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Warehouse": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Brand": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Customer Group": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"UOM": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Sales Partner": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"Sales Person": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},
	"User": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_master",
	},

	"Sales Order": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Delivery Note": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Sales Invoice": {
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Stock Entry":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Material Request":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Purchase Order":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Production Order":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Purchase Receipt":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Purchase Invoice":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Journal Entry":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Payment Entry":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Stock Reconciliation":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	},
	"Landed Cost Voucher":{
		"on_update": "sync_management.sync_management.sync_server_settings.sync_save_document",
		"on_submit": "sync_management.sync_management.sync_server_settings.sync_submit_document",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sync_management.tasks.all"
# 	],
# 	"daily": [
# 		"sync_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"sync_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sync_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sync_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sync_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sync_management.event.get_events"
# }
