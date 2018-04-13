FROM python:2.7.11
ADD test.py /
RUN pip install mysqlclient
CMD [ "python", "./test.py" ]
