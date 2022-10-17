FROM python:latest

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
VOLUME /app
WORKDIR /app

EXPOSE 5000
COPY code/api.py .

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]