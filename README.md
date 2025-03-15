# Flask - creating API part 8

## About

This repository is my tenth homework assignment from the Python Pro course. 

Celery is an asynchronous task queue/job queue based on distributed message passing. 
It is used to execute tasks concurrently, enabling the parallel processing of background jobs such as sending emails, processing images, or any other long-running tasks.

RabbitMQ is an open-source message broker that facilitates communication between distributed applications.
It uses a message queuing protocol (AMQP) to route messages between producers and consumers, ensuring reliable message delivery and enabling systems to handle asynchronous processing efficiently.

I have implemented celery and rabbitmq into the project.
- Added celery in docker-compose.yml
- Added rabbitmq in docker-compose.yml
- Added celery_tasks.py
- Updated views.py


## How to Run
Clone the repository:
  - git clone https://github.com/OleksiiUzu/flask-api-homework-10-celery-rabbitmq.git
  - cd flask-api-homework-10-celery-rabbitmq


2.(Optional) Create and activate a virtual environment:
  - python -m venv venv
  - source venv/bin/activate

3.Build the Docker image:
  - docker build -t flask-app .

4.Run the container:
  - docker run -p 5000:5000 flask-app
