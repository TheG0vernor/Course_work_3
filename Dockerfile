FROM python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run.py .
RUN python3 run.py -h 0.0.0.0 -p 80