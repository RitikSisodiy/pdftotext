# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY . .

# Set the environment variables (if needed)
# ENV FLASK_APP=app.py
# ENV FLASK_ENV=production

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Start Gunicorn
CMD ["sh","entry_point.sh"]
