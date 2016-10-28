# theitsociety

## Dependencies

- Python 3.x
- Python-pip (ensure that this is the version of pip for python3!)

## Installing the requirements
Dead simple, once python3 and pip are installed, just run:
```
pip3 install -r requirements.txt
```
If this fails to work, try:
```
pip install -r requirements.txt
```

## Ensure that you've created the superuser
Very important if you want to add some content to the website. It can be added and managed at $site.com/admin. Create the superuser so that you can login and add more users with different levels of access.
```
django-admin create superuser
```

## Running the server
In theitsociety/ run:
```
python3 manage.py runserver
```
And go to 127.0.0.1:8000

If you want this to be accessible to to the world, run:
```
python3 manage.py runserver 0.0.0.0:$port
```
Where $port is the port that you wish to access the website from. Ensure that it's forwarded!
