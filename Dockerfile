# Dockerfile
# Using the official Python 3.7 image
FROM python:3.7
# Set the Work Directory
WORKDIR /usr/src/app

# Install the project's dependencies
RUN pip install graphql_server
RUN pip install Flask
RUN pip install graphene
# Copy the project codes into the Work Directory
COPY . /usr/src/app

# Run the Flask application
CMD ["python3", "app.py", "runserver"]