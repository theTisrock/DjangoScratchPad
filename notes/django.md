HOW TO DJANGO

Install
	[command] pip (or pipenv) install django

Create a django project -
	create a directory to house the project: [command] mkdir my_project
	cd into my_project
	[command] django-admin.py startproject app_name .

Add a django app to the project - 
	[command] python manage.py startapp name_of_app 
		-this is a sub-packaged app that is scaffolded and snapped into the main django 'app'
	add the name of the app you just created into the 'INSTALLED_APPS' python list in settings.py

Run django in dev mode / dev server- 
	[command] python manage.py runserver

Migrate db migration scripts to the database - 
	[command] python manage.py migrate

Create a superuser for django-admin?
	[command] python manage.py createsuperuser
	follow the prompts

FILES and their purpose

manage.py - used to run commands in the shell environment
urls.py - used to setup routes
settings.py - register apps, configure databases, 
__init__.py - python package indicator
apps.py - configuration
models.py - database modeling
tests.py - testing
views.py - views


What is a Django "app"? -

	- Django overuses the term 'app'. Creating a new app inside of our project enables the reuse of that app within the same project or an entirely different project.

Urls.py - where the things are

	The BIG IDEA: The top level urls.py module in the "todo_app" package has the function 'include()' imported. Include links bottom level app urls to the top so they can be managed from the bottom in detail.
	When you add another app, make sure to tie in that app with this top level urls module.
	
	See the pattern???
	path(base_route, subsequent_patterns)
	path('admin', subsequent_patterns)  # admin
	path('', subsequent_patterns)  # root

	- Default routes: root "/", admin "/admin"
	- Default location: Project/main_app/urls.py
	- Subsequent routes can be created within the individual 'apps' that we create alongside the main app. 
	- Routes are in a python list called 'urlpatterns'. Importing the 'include()' function allows for bringing in routes/urls from different locations. This way urls can be managed at the individual app level instead of in the main app.

Views.py - what the things are

Observations about urls and views between flask and django -
Django creates a separation between the routes (urls.py) and the views/controllers (views.py) and templates.
Flask couples routes+views/controllers and only separates templates.


How do urls, views & templates interact? Urls map to functions called views that perform some task. When the task is completed, the state after execution of the view is applied to the template via render() and is returned in a response.
BIG IDEA: Url patters map to functions/views, functions/views map to templates

3 layers:

1 Url - endpoint for request
2 Views/controllers/functions - perform some action
3 Templates - package and send response

Change: mark item as done by striking through items, mark items as undo by removing the strike through.

components involved in the change: click(http request) -> url -> view/controller -> model -> template
template: 1) text for done/undo