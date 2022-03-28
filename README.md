# API
A list and retrieve endpoint built using Django REST as the backend framework.
There is a `requirements.txt` file in the project root directory where all the required dependencies have been specified.

# Language Framework and URL's:
Python version::3.10.2
Django==4.0.3
djangorestframework==3.13.1


Django Project: `Zattoo`
App name: `tenants`
 
All the data is stored in the django's default `SQLite` database.

For formatting tools, `black` has been installed and configured in the `settings.json`.

Important commands:

`python manage.py runserver`: to run the server, port and host specified in the settings.py file.

`http://127.0.0.1:8000/api/tenants/`:list endpoint, renders all available tenants as per the task.

`http://127.0.0.1:8000/api/tenants/%3C2%3E_TENANT_B/`:retrieve endpoint, Ex: for TENANT_B in this case.

`http://127.0.0.1:8000/admin/`: Admin View Page.
Required Credentials to log into the admin panel:
username: `admin`
password: `admin123`






