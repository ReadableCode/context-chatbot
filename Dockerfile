FROM python:3

# Install the required Python packages
COPY requirements.txt ./
RUN pip install --user -r requirements.txt

# set workdir
WORKDIR /app

# Copy the source code into the Docker container
COPY src/ src/

# Set the entry point for the Docker container
ENTRYPOINT ["python3", "src", "question_answering.py"]