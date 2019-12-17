FROM python:3.7-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api:app"]