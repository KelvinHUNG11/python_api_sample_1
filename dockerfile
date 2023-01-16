FROM python:3.9.5
ADD . /app
WORKDIR /app

COPY . .

RUN apt-get update \
    && pip --no-cache-dir install pipenv \
    && pipenv install
    
EXPOSE 3000

ENTRYPOINT [ "pipenv", "run", "python", "app.py"]