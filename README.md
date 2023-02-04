[![Testing with Github Actions](https://github.com/nigelmalaba1/WebApp/actions/workflows/main.yml/badge.svg)](https://github.com/nigelmalaba1/WebApp/actions/workflows/main.yml)


# Cloud Continuous Delivery of Flask Microservice 
Breakfast Menu Web App using Flask Microservice

## Project Summary 

in this project, I created a Microservice app in Flask and configured a Build System to Deploy changes. 

I used IaC *(Infrastructure as Code)* to deploy code in AWS App Runner.

This microservice generates a nutritious breakfast menu according to the user's inputs. The service will suggest appropriate food options considering factors such as the user's level of fatigue and the day of the week, for example if the user is tired, the microservie will recommend coffee and other items that will help the user becoem more focused throughout the day. The goal of the microservice is to eliminate the need to make a daily breakfast decision and free up the user's time and energy for more important matters.


## Command Line Steps

Create virtualenv 'python3 -m venv <name_of_virtual_environment>'

Install: Run 'make install'

Run the app: 'python3 app.py'

## Docker Commands

'https://github.com/nigelmalaba1/Breakfast-Microservice-with-Flask.git'

'docker build -t myflaskmicroservice .'

'docker run -p 8080:8080 myflaskmicroservice'

# Architecture Diagram 

+-----------------------+         +---------------+
|                       |         |               |
|   Github Codespaces|           | AWS App Runner|
|                       |         |               |
+-----------------------+         +---------------+
      |                                           |
      |                                           |
      |   Push code changes to Git Repository     |
      |-------------------------------------------|
      |                                           |
      |                                           |
+-----------------------+         +---------------+
|                       |         |               |
|     Git Repository    |         |     AWS EC2   |
|                       |         |  Instance     |
+-----------------------+         +---------------+
      |                                           |
      |                                           |
      |   Code changes trigger App Runner         |
      |   deployment pipeline                      |
      |-------------------------------------------|
      |                                           |
      |                                           |
+-----------------------+         +---------------+
|                       |         |               |
|   Flask Microservice  |         |     Nginx     |
|   deployed on EC2     |         |    Reverse    |
|                       |         |    Proxy      |
+-----------------------+         +---------------+
      |                                           |
      |                                           |
      |   Web Application with Login Page         |
      |   served to end-users                     |
      |                                           |
      +------------------------------------------------




