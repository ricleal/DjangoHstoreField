# DjangoHstoreField
Django test with a Model with HStoreField and the respective ModelForm.

HStore fiels supports not nested strings json . Sort of is OK:
```
{"att2": "{'a':'2','b':'3'}", "att1": "2"}
```
(Note the double quotes!!!)

# To start the project

```
django-admin startproject site1
cd site1/
python manage.py startapp plot1
```
# Then

Edit DB stuff...

then:
```
python manage.py migrate
python manage.py makemigrations
```

Using ```pgcli```, something like this should show up:

```
$ pgcli mydb user1
Password:
Version: 0.19.1
Chat: https://gitter.im/dbcli/pgcli
Mail: https://groups.google.com/forum/#!forum/pgcli
Home: http://pgcli.com
mydb> \dt
+----------+----------------------------+--------+---------+
| Schema   | Name                       | Type   | Owner   |
|----------+----------------------------+--------+---------|
| public   | auth_group                 | table  | user1   |
| public   | auth_group_permissions     | table  | user1   |
| public   | auth_permission            | table  | user1   |
| public   | auth_user                  | table  | user1   |
| public   | auth_user_groups           | table  | user1   |
| public   | auth_user_user_permissions | table  | user1   |
| public   | django_admin_log           | table  | user1   |
| public   | django_content_type        | table  | user1   |
| public   | django_migrations          | table  | user1   |
| public   | django_session             | table  | user1   |
+----------+----------------------------+--------+---------+
SELECT 10
Command Time: 0.000s
Format Time: 0.004s
mydb>
```

# Then

```
python manage.py makemigrations --empty test1
```

edit
site1/migrations/0001_initial.py

Then:
```
python manage.py migrate
```

# Add a model with HStore field, then:

```
python manage.py makemigrations
python manage.py migrate
```


# create super user:
```
python manage.py createsuperuser
```
pass: admin/admin

add models to admin.py

# Open admin

python manage.py runserver

http://127.0.0.1:8000/admin

# Run:
```
python manage.py runserver
```
Open the browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


# Valid urls:
http://localhost:8000/test1/detail/11/
http://localhost:8000/test1/list
http://localhost:8000/test1/create


# Tested:
with:
- Django 1.8.3


# Reference:
http://matthewdaly.co.uk/blog/2015/08/01/exploring-the-hstorefield-in-django-1-dot-8/
