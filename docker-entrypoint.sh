#!/bin/sh

echo "🔄 Running Alembic migrations..."
alembic upgrade head

echo "🚀 Starting FastAPI app..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT} --log-level debug
