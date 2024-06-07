# Stage 1: Build stage
FROM python:3.9-slim as build-stage

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=build-stage /app /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run streamlit app
CMD ["streamlit", "run", "Pagina_Principal.py", "--server.port", "8080"]
