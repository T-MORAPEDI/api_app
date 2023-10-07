# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables for Django (customize as needed)
ENV DJANGO_SETTINGS_MODULE=core.settings
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application's code into the container
COPY . /app/

# Expose the port that the application will run on (customize if needed)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver"]