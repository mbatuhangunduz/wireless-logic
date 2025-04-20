#!/bin/sh
echo "🧾 Available migration files:"
ls -la ./migrations/versions
echo "🔄 Running Alembic migrations..."
alembic upgrade head

echo "🚀 Starting FastAPI app..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT} --reload --log-level debug
