FROM python:3.8.5-slim-buster@sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3

WORKDIR /usr/src/app


COPY requirements/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/application"

CMD ["gunicorn","--bind","0.0.0.0:8000", "-w", "4", "app:app"]
