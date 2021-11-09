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

# create file for database
RUN rm webapp/database/db.sqlite3
RUN touch webapp/database/db.sqlite3


# install requirments
RUN pipenv install --skip-lock --system --dev

# makes massmine executable
#RUN ln -s `pwd`/massmine /usr/local/bin


# execute startup script
CMD ["bash", "startup.sh"]


