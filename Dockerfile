FROM python:slim

RUN useradd blog

WORKDIR /home/blog

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y postgresql 
RUN apt-get install -y libpq-dev gcc
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY blog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP blog.py
RUN chown -R blog:blog ./
USER blog

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]