# syntax=docker/dockerfile:1
FROM python:3.7-alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
RUN echo '🐱'
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]