FROM debian:bullseye-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    apache2 \
    python3 \
    python3-pip \
    python3-dev \
    libmariadb-dev \
    libapache2-mod-wsgi-py3 \
    pkg-config \
    gcc 
    
# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


WORKDIR /app

COPY ./app /app
RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD [ "apachectl", "-DFOREGROUND" ]
