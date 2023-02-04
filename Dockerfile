# Use the official Python image as the base image
FROM python:3.7

# Set the working directory
WORKDIR /webapp

# Copy the Flask microservice code into the image
COPY . /webapp

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=webapp.py

# Expose port 8080 for the Flask microservice
EXPOSE 8080

# Run the Flask microservice
CMD ["flask", "run", "--host=0.0.0.0"]
