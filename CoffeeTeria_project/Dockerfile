# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory for the backend
WORKDIR /app/BackEnd

# Copy requirements.txt and install Python dependencies
COPY BackEnd/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the backend application code
COPY BackEnd/ .

# Set the working directory for the frontend
WORKDIR /app/FrontEnd

# Copy the frontend package.json and install Node.js dependencies
COPY FrontEnd/CoffeeTeria/package.json FrontEnd/CoffeeTeria/package-lock.json ./
RUN npm install

# Copy the rest of the frontend application code
COPY FrontEnd/CoffeeTeria/ .

# Expose the ports for the backend (8000) and frontend (3000)
EXPOSE 8000 3000

# Install supervisor to manage both processes
RUN pip install supervisor

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Command to run the supervisor
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
