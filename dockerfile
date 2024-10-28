FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libffi-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy files
COPY app_run.py ./
COPY requirements.txt ./
COPY rf_final_model.joblib ./
COPY scaler.joblib ./

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install Cython
RUN pip install Cython

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your application
CMD ["streamlit", "run", "app_run.py", "--server.port=8501", "--server.address=0.0.0.0"]
