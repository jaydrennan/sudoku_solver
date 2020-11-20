FROM python:3.8.5-slim-buster@sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3

WORKDIR /usr/src/app

COPY requirements/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "application/app.py"]