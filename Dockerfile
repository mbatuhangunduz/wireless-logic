
FROM python:3.12-slim

# Ortamı ayarla
WORKDIR /app

# Gerekli paketler (gettext -> envsubst için)
RUN apt-get update && apt-get install -y gettext

# Gerekli dosyaları kopyala ve kurulum yap
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projeyi içeri al
COPY . .

# Ortam değişkenleri
ENV PORT=80

# Entry point script'i çalıştır
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
