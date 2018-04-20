FROM python:2.7.11
LABEL maintainer justin@gokhalemethod.com
WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD [ "python", "test.py" ]

CMD [ "bash" ]
