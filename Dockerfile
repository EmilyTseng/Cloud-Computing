# Week 2
FROM python:3.10.7
USER root

RUN pip3 install jupyter
RUN apt-get update && apt-get install wget

ENV JUPYTER_USER emily
RUN useradd -ms /bin/bash ${JUPYTER_USER}

RUN mkdir -p /home/emily

WORKDIR /home/emily
RUN wget -c https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Financial%20Statement%20Analysis%202.ipynb -O TEST.ipynb

RUN chown ${JUPYTER_USER}: /home/emily
RUN chmod 777 /home/emily

USER ${JUPYTER_USER}

EXPOSE 8888

CMD jupyter notebook --ip=0.0.0.0 --port 8888 --allow-root

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /