FROM python:3.9

WORKDIR /app

COPY ./app .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r /app/requirements/requirements.txt

EXPOSE 3003
EXPOSE 5000

COPY bootstrap.sh /etc/bootstrap.sh
RUN chmod a+x /etc/bootstrap.sh

CMD ["/etc/bootstrap.sh"]