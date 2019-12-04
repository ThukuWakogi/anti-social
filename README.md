# anti-social

[anti-social](https://thukuwakogi.github.io/anti-social-face/) is an app that keeps you updated on events in your neighbourhood and allows to also keep others updated

## author

Timothy Oliver [@ThukuWakogi](https://github.com/ThukuWakogi)

## features

1. login, register and sign out
2. view and join neighbours
3. add posts

## SetUp

To view a demo of the application, click [here](https://thukuwakogi.github.io/anti-social-face/).

The source code for this application can be accessed.

a copy of the source code can be gotten through:

- downloading the zip from github.
- opening a terminal in the preferred directory then entering `git clone https://github.com/ThukuWakogi/anti-social.git`
- using a git client such as [Github desktop](https://desktop.github.com/) or [GitKraken](https://www.gitkraken.com/)

### installing

#### windows

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python -m venv virtual`
* Activating the virtual environment may change based on the terminal or shell being used.
* For command prompt, enter `virtual\Scripts\activate` or simply type in activate.
* For powershell, the execution policy should be bypassed for the script to run. This can be done by entering `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then proceeding on with entering .`.\virtual\Scripts\Activate.ps1`
* Install packages. `pip install -r requirements.txt`
* open a psql client and create a database called filtered_lenses `CREATE DATABASE antisocial;`
* Setting environment variables differs with the terminal or shell being used
* Declare environment variables to be used by the app during run time
  - `$env:DB_USER="<database user>"`
  - `$env:DB_PASSWORD="<database password>"`
  - `$env:DB_Name="<database name>"`
* make the migration files `python manage.py makemigrations gallery`
* migrate the database `python3.6 manage.py migrate`
* then start the server `python manage.py runserver`

#### unix

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python3.x -m venv --without-pip virtual` replace x with version in host machine, preferably version v3.6 for this project
* Activate the virtual environment `source virtual/bin/activate`
* Download pip into the virtual environment `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install packages. `pip install -r requirements.txt`
* open a psql client and create a database called filtered_lenses `CREATE DATABASE antisocial;`
* make the migration files `python manage.py makemigrations gallery`
* migrate the database `python3.6 manage.py migrate`
* start the server `python3.x manage.py runserver`

## Development tools
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Angular](https://angular.io/)
* [Angular Material](https://material.angular.io/)
* [Postgresql](https://www.postgresql.org/)
* HTML
* CSS

## license
This project is under the MIT license. click [here](https://github.com/ThukuWakogi/anti-social/blob/master/LICENSE) for more details
