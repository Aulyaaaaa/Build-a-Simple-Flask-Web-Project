# syntax=docker/dockerfile:1

FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Install dependencies untuk build package Python (jika ada C-extension)
RUN apk add --no-cache build-base libffi-dev linux-headers

# Copy file requirements.txt terlebih dahulu agar cache build efisien
COPY requirements.txt .

# Install dependencies Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh isi folder proyek ke dalam container
COPY . .

# Set environment agar Flask mengenali app
ENV FLASK_APP=board
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

# Jalankan aplikasi Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

# Buka port Flask
EXPOSE 5000



