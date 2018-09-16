FROM python:latest

RUN apt-get update && apt-get -qq install redis-tools

RUN pip install redis

COPY redistest.py /usr/local/etc/redistest.py

CMD [ "python", "/usr/local/etc/redistest.py" ]

# CMD [ "/bin/bash" ]