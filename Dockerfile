FROM python:3.10

RUN apt-get update && apt-get install telnet \
                                      nano


COPY ./requirements.txt /home/requirements.txt
WORKDIR /home/
ENV PYTHONPATH=/home/
RUN pip install -r requirements.txt


CMD ["tail","-f","/dev/null"]

