FROM python:3.12-alpine

# Install build tools and dependencies
RUN apk update && apk add --no-cache \
    python3-dev \
    gcc \
    musl-dev \
    libjpeg-turbo-dev \
    freetype-dev \
    libpng-dev \
    sdl2-dev \
    sdl2_image-dev \
    sdl2_mixer-dev \
    sdl2_ttf-dev \
    bash

# Set working directory
WORKDIR /app

# Copy your source files
COPY app/ ./app/
COPY images/ ./images/

# Install pygame (build from source)
RUN pip install --no-cache-dir pygame

# Run your game
CMD ["python", "app/alien_invasion.py"]
