# Use an official Python runtime as a parent image
FROM python:3.11.3-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Get the latest MiKTeX image from the registry
RUN docker pull miktex/miktex

# Create a Docker volume named miktex
RUN docker volume create --name miktex

# Provided that your main input file is located in the current working directory, you can run pdflatex as follows
RUN docker run -ti \
  -v miktex:/miktex/.miktex \
  -v `pwd`:/miktex/work \
  miktex/miktex \
  pdflatex main.tex

# Expose the port that the Django development server will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

