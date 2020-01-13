# Start project iCastle
~/dev/src/3d> 
django-admin startproject iCastle .

# allowed hosts

# run.sh
cat >> run.sh
python manage.py runserver 0.0.0.0:8000

# migrate, superuser
python manage.py migrate
python manage.py createsuperuser

# views, templates, urls
