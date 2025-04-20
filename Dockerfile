FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 🔧 Kopyalanması gereken her şeyi açıkça belirtelim
COPY app ./app
COPY migrations ./migrations
COPY alembic.ini .
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

ENV PORT=80

ENTRYPOINT ["/docker-entrypoint.sh"]
