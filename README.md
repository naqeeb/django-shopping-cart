Welcome to the wonderful world of django shopping carts.  To get started you will need to do the following:

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

### Requirements
* MySql

### Setup

python manage.py migrate

python manage.py loaddata fixtures/initial_data.json

python manage.py runserver

