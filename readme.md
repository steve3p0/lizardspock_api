## The Lizard Spock Expansion: Flask Web API

This project is a Rock, Paper, Scissors web API implementation of the game popularized by an 
episode an episode of "The Big Game Theory" expanded to include a lizard and Spock from Star Trek.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
* Python 3.6 or greater
* PIP3
* Python 3 Virtual Environment (python3-venv)
* Flask
* Flask-RESTful

IDE:
I use PyCharm, and provided the recommended files in ```/.ida``` folder [here](https://github.com/steve3p0/lizardspock/tree/master/lizardspock_api/.idea).

### Installing

If you don't have Python 3 installed, start [here](https://wiki.python.org/moin/BeginnersGuide/Download).

For the rest of the requirements:
```
sudo apt-get update
sudo apt-get install python3-pip
sudo apt install python3-venv
pip3 install flask
pip3 install Flask-RESTful
pip3 install typing
```

Create the python virtual environment:
```
virtualenv --python=python3 
sudo apt-get update
sudo apt-get install python3-pip
sudo apt install python3-venv
pip3 install flask
pip install Flask-RESTful
```


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc



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