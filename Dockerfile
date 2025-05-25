# Use base image of python
FROM python:3.9 

# Set the working directory
WORKDIR /app

# copy project files
COPY . .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Command to run the chatbot API
CMD ["unicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]