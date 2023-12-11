# ./api-gateway/Dockerfile
FROM python:3.8

WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Expose the port that the application will run on
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]
