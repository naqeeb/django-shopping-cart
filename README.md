Welcome to the wonderful world of django shopping carts.  To get started you will need to do the following:

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

### Setup Sites and Stores (Django Admin)

Store 1 | domain: store1.example.com

Store 2 | domain: store2.example.com

Store 3 | domain: store3.example.com

### Host File
Create host file entries to mimic multiple domain setup. You will need to specific the port that your running on (locally)
For Mac OS X: edit etc/hosts file

127.0.0.1 store1.example.com

127.0.0.1 store2.example.com

127.0.0.1 store3.example.com

In separate terminals run the following commands

### Store 1

python manage.py syncdb --settings django_ecommerce.settings.store1

python manage.py migrate --settings django_ecommerce.settings.store1

python manage.py loaddata fixtures/initial_data.json --settings django_ecommerce.settings.store1

python manage.py runserver 8000 --settings django_ecommerce.settings.store1

### Store 2

python manage.py syncdb --settings django_ecommerce.settings.store2

python manage.py migrate --settings django_ecommerce.settings.store2

python manage.py loaddata fixtures/initial_data.json --settings django_ecommerce.settings.store2

python manage.py runserver 8001 --settings django_ecommerce.settings.store2



