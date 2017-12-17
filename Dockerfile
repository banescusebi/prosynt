# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory
WORKDIR /prosynt

# Copy the current directory contents into the container at /prosynt
ADD . /prosynt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "prosynt.py"]
