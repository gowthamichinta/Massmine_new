ln -s `pwd`/massmine /usr/local/bin
python3 webapp/manage.py migrate
python3 webapp/manage.py runserver 0.0.0.0:8000