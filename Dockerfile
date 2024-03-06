# FROM python:3.11.8-slim
# WORKDIR /app
# COPY ./requirements.txt /app
# RUN pip install -r requirements.txt
# COPY . .
# EXPOSE 5000
# ENV FLASK_APP=app.py
# CMD ["flask", "run", "--host", "0.0.0.0"]
FROM python:3.11.8-alpine

WORKDIR /usr/src/app

COPY . .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps



CMD ["python3", "app.py"]

EXPOSE 8080
