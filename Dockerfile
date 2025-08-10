FROM python:3-slim

# Install system dependencies for pygame and X11
RUN apt-get update && \
    apt-get install -y python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libsm6 libxext6 libxrender-dev libgl1-mesa-glx x11-apps && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project files
COPY app/ ./app/
COPY images/ ./images/

# Install Python dependencies
RUN pip install --no-cache-dir pygame

# Set the entrypoint
CMD ["python", "app/alien_invasion.py"]