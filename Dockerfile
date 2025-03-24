# Python 3.12 base image for better performance and security
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies file
COPY requirements.txt .

# Install dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the container
COPY . .

# Ensure wait-for-it script is present for database readiness check
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Command to start FastAPI and run tests in parallel
CMD ["/wait-for-it.sh", "db:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
