# Django Sample App

Python Django MVC sample app showing restaraunt reservations for restaraunt tables and food menu items. Using Bootstrap & JQuery on the frontend and demonstrating Create/Read/Update/Delete routes for each object. There is  a login and registration system, with members-only access.


###Setup

Setup your database in config/settings.py: SQLite file is used default, but can be changed to mysql. Then inject the SQL to begin. Open Command Prompt and cd to the project directory. To inject the SQL models into db.sqlite3, execute:

```python manage.py sql sessions auth app | python manage.py dbshell```


If there are any pre-existing models, clear them with 

```python manage.py sqlclear sessions auth app | python manage.py dbshell```

To tun the server execute: 
```python manage.py runserver 80```

###Explanations

config/urls.py -- contains url paths that trigger the controllers such as: app.controllerFileName.method 

app/\*.py -- each view-rendering controller has a separate file with methods

app/models.py -- set this up for each object model, then run ```python manage.py sql app```

views/base.html-- default layout which links to the static css/js, and is extended by blocks: title, content, head (where to include page js )

views/header.html -- global header bar, you can change active tab and with username/login

views/\*/\*.html -- views returned for each controller, extending base.html with these blocks: title, content, head

static/ -- contains JQuery & Bootstrap and global.css included in base.html for all the pages