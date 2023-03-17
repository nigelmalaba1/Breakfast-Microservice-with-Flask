[![Testing with Github Actions](https://github.com/nigelmalaba1/WebApp/actions/workflows/main.yml/badge.svg)](https://github.com/nigelmalaba1/WebApp/actions/workflows/main.yml)


# Cloud Continuous Delivery of Flask Microservice 
Breakfast Menu Web App using Flask Microservice 

AWS App Runner Default Domain:

(https://ku934wgxji.us-east-1.awsapprunner.com)


# Flask Breakfast Microservice
A Flask microservice that suggests breakfast items for each day of the week based on user input. This microservice is hosted on AWS App Runner, and it's built on Codespaces using Python.

This microservice generates a nutritious breakfast menu according to the user's inputs. The service will suggest appropriate food options considering factors such as the user's level of fatigue and the day of the week, for example if the user is tired, the microservie will recommend coffee and other items that will help the user becoem more focused throughout the day. The goal of the microservice is to eliminate the need to make a daily breakfast decision and free up the user's time and energy for more important matters.

# Routes
## Login

This microservice has a login page, where users can input their username and password. If the credentials are correct, the user is redirected to the welcome page. Otherwise, an error message is displayed.

## Welcome
This page is displayed when the user successfully logs in. It serves no other purpose.

## Root
If the user goes to the root path /breakfast, a function returns a string with one breakfast item, one day of the week, one fruit, and one beverage.

## Dontrepeat
If the user goes to the /breakfast/dontrepeat path, a function returns a string with two breakfast items, without repeating any of the previous suggestions.

## Tired
If the user goes to the /breakfast/tired path, a function returns a string with one breakfast item and one beverage, suitable for someone who is tired.

## Day of the Week
If the user goes to the /breakfast/<day> path, a function returns a string with a breakfast item, a fruit, and a beverage, suitable for that specific day of the week. On Saturdays, the function suggests the user can eat anything they want. On Sundays, the function suggests the user eat some fruits before the start of the week. On all other days, the function suggests the user eat oatmeal.

# How to Run

Create virtualenv `python3 -m venv <name_of_virtual_environment>`

Clone this repository.

Install Python, Flask, and the required dependencies.

Install: Run `make install`

Run `python3 app.py`.

Access the microservice at http://localhost:8080.


## Docker Commands

1. Git Clone: `https://github.com/nigelmalaba1/Breakfast-Microservice-with-Flask.git`

2. `docker build -t myflaskmicroservice .`

3. `docker run -p 8080:8080 myflaskmicroservice`

4. Test the Flask microservice by accessing it in a web browser at `(http://localhost:8080)`

# Architecture Diagram 

![Blank diagram (1)](https://user-images.githubusercontent.com/123284219/217413980-3af7e0d9-ad16-407f-b8b3-b4b30a7d5395.jpeg)


![websequence1](https://user-images.githubusercontent.com/123284219/224525073-462e0d20-731e-4464-af78-9471d97c9476.jpeg)


# Future Improvements

Add the option for users to suggest their own breakfast items.
Create a database to store user preferences and suggest more personalized breakfast items.
Improve the UI of the login and welcome pages.
