# Dockerizd Python RQ + FastAPI 

This is an example of a Dockerized version of FastAPI + Python RQ. More information can be found in the blog post [here](https://blog.devgenius.io/efficient-background-job-processing-with-docker-python-fastapi-and-redis-queue-with-an-example-8eb0c6188981)

It includes:
1. app/api.py - The API layer that allows user to submit a job to the queue, and query the status of a job via API endpoints
2. app/jobs.py - Contains the job logic
3. Dockerfile - Basic Dockerfile to setup the API + worker container
4. docker-compose.yml - Compose file that links Redis + FastAPI + worker together


To run, simply execute `docker-compose up --build` in your terminal, and you should have access to the endpoints via localhost:8000.

You can also run multiple instance of workers via `docker-compose up --build --scale worker=N` where N is the number of instances you would like to run, eg: 3. 