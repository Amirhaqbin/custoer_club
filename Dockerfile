FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /cheestore
WORKDIR /cheestore
COPY . /cheestore

# Installing requirements
ADD requirements/requirements.txt /cheestore
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "cheestore", "--bind", ":8000", "cheestore.wsgi:application"]










# FROM python:3.4

# RUN apt-get update \
# 	&& apt-get install -y --no-install-recommends \
# 		postgresql-client \
# 	&& rm -rf /var/lib/apt/lists/*

# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .

# EXPOSE 8000
# ADD    ./manage.py      /app/

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# FROM python:3.8-alpine 

# WORKDIR /app
RUN     pip install --upgrade pip
# ADD    ./requirements.txt   /app/
# RUN    pip install -r requirements.txt
# RUN   apk update && apk add bash
# RUN   apk add --no-cache bash

# # ADD    ./djangosample   /app/djangosample/
# ADD    ./gunicorn       /app/gunicorn/

# CMD ["djangosample.wsgi","python3", "-c" ]
# # "gunicorn","gunicorn/prod.py"