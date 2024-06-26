FROM python:3.11.4

ENV GECKODRIVER_VER=v0.31.0
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

RUN useradd --create-home --home-dir /home/flaskapp enz

WORKDIR /home/flaskapp
RUN apt-get update && apt-get install -y iputils-ping wget

USER enz
RUN mkdir app

COPY ./app ./app
COPY ./app.py .

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --user -r requirements.txt
RUN pip install gevent gunicorn==22.0.0

EXPOSE 5000

CMD ["gunicorn", "--workers", "1", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "app:create_app()"]