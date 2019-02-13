FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip3 install requests
RUN pip3 install confluent-kafka
EXPOSE 4040

COPY ./app /app
