FROM python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run.py .
CMD python3 run.py -h 0.0.0.0 -p 80