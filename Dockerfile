FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

RUN pip install --upgrade pip

# Run unit tests
RUN python3 -m unittest test_calculator.py

# Set default command
CMD ["python3", "calculator.py"]
