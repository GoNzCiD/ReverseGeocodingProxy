FROM python:3.8.2-alpine3.11

COPY reversegeocodingproxy /home/www/reversegeocodingproxy/reversegeocodingproxy
COPY requirements.txt /home/www/reversegeocodingproxy
COPY run.py /home/www/reversegeocodingproxy

WORKDIR /home/www/reversegeocodingproxy

RUN pip install -r requirements.txt

ENV FLASK_CONFIGURATION prod

CMD ["gunicorn", "--bind", "0.0.0.0:8888", "run:app"]

EXPOSE 8888