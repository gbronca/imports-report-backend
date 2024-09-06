FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the scripts to the folder
COPY . /app

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]