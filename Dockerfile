FROM python:3.10-slim-bullseye

WORKDIR /app

# Install system dependencies required for OpenCV and YOLO
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy webapp source code
COPY src/webapp /app/src/webapp

# Copy model artifacts into the container 
# This requires the best.pt file to not be matched by .dockerignore completely.
# We copy it into a specific model directory within the container
COPY scripts/training/runs/train/26m/yolo_vertex_exp-7/weights/best.pt /app/model/best.pt

# Configuration environment variables
ENV MODEL_PATH=/app/model/best.pt
ENV PYTHONPATH=/app/src

EXPOSE 5000

WORKDIR /app/src/webapp

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-5000} --timeout 120 app:app"]