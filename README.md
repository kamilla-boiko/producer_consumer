# Producer - Consumer

This is a simple microservice implementation of a "Producer - Consumer" 
system using Django, PostgreSQL, and Celery. The goal of this project is 
to create a service where Celery adds a record to a model every minute. 
Users can then delete these records from the database using a web interface.

## Technologies Used

* Django
* PostgreSQL
* Celery
* Docker Compose

## Prerequisites

Before running the microservice in Docker, ensure you have the following installed on your machine:
* Docker: [Install Docker](https://docs.docker.com/get-docker/)
* Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started
1. Clone the repository to your local machine:
```
git clone git@github.com:kamilla-boiko/producer_consumer.git
cd producer_consumer
```

2. Create a .env file based on the provided .env_sample and update the necessary environment variables.

3. Build the Docker containers and start the application:
```
docker-compose up --build
```

## Environment variables

This project uses environment variables to store sensitive or configurable data.
The variables are stored in a file named .env, which should be created in the
project's root directory.
Please follow the instructions below to set up the environment variables for your local development.

### .env file

Create a file named .env in the root directory of the project and add the following variables
with their corresponding values.

### .env_sample file

A file named .env_sample is included in the repository as a template for setting up the .env file.
It contains the names of the environment variables without their values.
You can use it as a reference when creating your own .env file.
