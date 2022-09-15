FROM python:3.10

RUN apt-get update && apt-get install telnet

CMD ["tail","-f","/dev/null"]

