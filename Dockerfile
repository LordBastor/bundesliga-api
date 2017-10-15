FROM python:2.7

# Install geospatial libraries, not needed for now, but might be useful later
# RUN apt-get update
# RUN apt-get install -y binutils libproj-dev gdal-bin

ENV PYTHONUNBUFFERED 1

# Let's work in directory /code
RUN mkdir /code
WORKDIR /code

# Pre install Pillow so changes in requirements.txt doesn't take ages
RUN pip install Pillow==2.9.0

# Install python frameworks and libs from requirements.txt
# RUN apt-get install python-gdal
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Copy our files in current directory to /code, except files / dirs defined in .dockerignore
ADD . /code/

RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# Expose running containers on port 8000
EXPOSE 8000

# Run django server on port 8000 and allow traffic from anywhere
CMD python /code/bdlg_api/manage.py runserver 0:8000
