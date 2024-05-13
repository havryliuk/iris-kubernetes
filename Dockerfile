FROM python:3.10-slim

WORKDIR /app

ADD iris_app.py /app
ADD model.pkl /app
ADD requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "iris_app.py"]
