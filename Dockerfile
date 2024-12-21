# getting os and python official image from dockerhub
FROM python:3.9.13-slim-bullseye

WORKDIR /docker

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . . 

CMD ["python3", "-m", "flask", "--app", "loan", "run", "--host=0.0.0.0"]