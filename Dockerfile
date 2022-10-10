FROM python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run.py .
RUN python3 -m gunicorn run:app -b 0.0.0.0:80 -w 3