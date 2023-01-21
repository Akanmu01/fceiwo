pip install -r requirements.txt
python manage.py migrate --no-input
python manage.py collectstatic --no-input
# python3.9 manage.py collectstatic
# python3.9 manage.py makemigrations
# python3.9 manage.py migrate
# python3.9 manage.py runserver
