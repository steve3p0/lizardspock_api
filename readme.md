## The Lizard Spock Expansion: Flask Web API

This project is a Rock, Paper, Scissors web API implementation of the game popularized by an 
episode an episode of "The Big Game Theory" expanded to include a lizard and Spock from Star Trek.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
* Python 3.6 or greater
* PIP3 (python 3 installer)
* Python 3 Virtual Environment (python3-venv)
* nose (python unit and integration testing)
* Flask (web api)
* Flask-RESTful (web api rest library)
* Flask-CORS (enables Cross Origin Resource Sharing)
* Typing (for type hints)

IDE:
I use PyCharm, and provided the recommended files in ```/.ida``` folder [here](https://github.com/steve3p0/lizardspock/tree/master/lizardspock_api/.idea).

### Installing

If you don't have Python 3 installed, start [here](https://wiki.python.org/moin/BeginnersGuide/Download).

For the rest of the requirements:
```
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo apt install python3-venv
$ pip3 install nose
$ pip3 install flask
$ pip3 install Flask-RESTful
$ pip3 install -U flask-cors
$ pip3 install typing
```

Navigate to where you want to create the project directory and virtual environment:
Create the project folder and virtual environment:
```
$ virtualenv --python=python3 lizardspock_api
```

Pull this repo into the project directory:
```
$ git clone git@github.com:steve3p0/lizardspock_api.git
```

## Running the tests

Run the tests with this command:

```
$ nosetests
```
### Running the web api on your local machine
You can run this on your local machine:
```
$ flask run
```

## Deployment
Coming soon... 

## Rock Paper Scissors Spock: Web Service API
Here are the requirements for the Web Service API.

### Choices
Get all the choices that are usable for the UI.

	• GET: /choices

```Result: application/json
[
  {
    "choice": {
      “id": integer [1-5],
      "name": string [12] (rock, paper, scissors, lizard, spock)
    }
  }
]
```

### Choice

Get a randomly generated choice (for clients that don’t trust the server)

	• GET: /choice

```Result: application/json
{
  "id": integer [1-5],
  "name" : string [12] (rock, paper, scissors, lizard, spock)
}
```

### Play

Play a round (for servers that don’t trust the client)

	• POST: /play

```
Data: application/json
{
  “player”: choice_id 
}

Result: application/json
{
  "results": string [12] (win, lose, tie),
  “player”: choice_id,
  “computer”:  choice_id
}
```