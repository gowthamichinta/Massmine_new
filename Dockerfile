FROM debian

RUN mkdir /app
WORKDIR /app
ADD . /app/

# install python, pip, enchant, pipenv
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        libenchant-2-2
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# install requirments
RUN pipenv install --skip-lock --system --dev

# makes massmine executable
RUN ln -s `pwd`/massmine /usr/local/bin

# create file for database
RUN touch webapp/db.sqlite3

# execute startup script
CMD ["bash", "startup.sh"]


