# Django User Profile

Django project that allows basic login/logout functionality. 

<br />

## Usage

```bash
$ # Clone
$ git clone https://github.com/app-generator/django-user-profile.git
$ cd django-user-profile
$
$ # Create virtual environment (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ python -m virtualenv env
$ .\env\Scripts\activate
$
$ # Install required modules
$ pip install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start application 
$ python manage.py runserver
$
$ # Starting the app in custom port if 8000 is occupied
$ python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access in browser: http://127.0.0.1:8000/
```

> You will need to register first before you can use it.

<br />

## Code Structure

The project uses the following structure:

```bash
ROOT DIR

- core/                                                     # Configures necessary files
|            -settings.py
|            -urls.py
|            -wsgi.py
|            -asgi.py
|            -__init__.py
|            -templates
|                        -accounts/
|                                    -login.html
|                                    -register.html
|                        -includes/
|                                    -footer.html
|                                    -navigation.html
|                                    -scripts.html
|                                    -sidebar.html
|                        -layouts/
|                        -dashboard.html
|            -static/
|                    -assets
|                            -css/
|                            -img
|                            -js/
|                            -vender
|
-authentication/                                            # Authenticates users
|
-app/                                                       # App that gives signed in users page access
|
-media/                                                     # Stores media uploaded by user
|            -customers/
|                        -profiles/
|
-customers/                                                 # App that deals with the user profile
|            -templates/
|                        -customers/
|                                    -profile.html
|            -admin.py
|            -forms.py
|            -urls.py
|            -views.py
|            -models.py
|            -signals.py
|
-env/
|
-manage.py                                                  # Default command script 
|
-requirements.txt                                           # Modules required before running.
|
```
return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
```
