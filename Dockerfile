FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir
COPY backend/ .
COPY .env .
CMD ["gunicorn", "test_stripe.wsgi:application", "--bind", "0:8000"]