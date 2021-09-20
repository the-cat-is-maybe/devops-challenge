# PeerIQ DevOps Challenge

This challenge was designed to look for your devops skills. This repository contains a simple python application. But it is not completed at all.
The app needs a mongodb database to be able to run it.

## The app

This is a python *(flask)* application. To download it:

```bash
git clone https://github.com/peeriq/devops-challenge.git
cd ./devops-challenge
```

### Run the tests

![Tox](./assets/tox.logo.png)

This python app contains some tests. To run it in your own host:

```bash
pip install tox
tox
___________________________________________________________________________________________ summary ___________________________________________________________________________________________
  py27: commands succeeded
  py37: commands succeeded
  py38: commands succeeded
```

If you prefer, you can run the tests in a container:

```bash
docker run -it -v $(pwd):/tmp/app -w /tmp/app --rm painless/tox /bin/bash tox
___________________________________________________________________________________________ summary ___________________________________________________________________________________________
  py27: commands succeeded
  py37: commands succeeded
  py38: commands succeeded
  congratulations :)
```

### Run the app

If you want to run the app locally:

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
export MONGO_URI=mongodb://YOUR_USERNAME:YOUR_PASSWORD@YOUR_MONGO_HOST:YOUR_MONGO_PORT/YOUR_MONGO_DB_NAME
python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

You will be able to access the api locally in the `8080` port.

#### The API

- `/api/v1/restaurant`: Returns a list containing all the restaurants.
- `/api/v1/restaurant/{id}`: Returns a list with a single restaurant that match the `id` path parameter.

Examples:

```bash
curl localhost:8080/api/v1/restaurant | jq
.
.
.
 {
    "URL": "http://www.just-eat.co.uk/restaurants-bayleafn9/menu",
    "_id": "55f14313c7447c3da7052249",
    "address": "61 Bounces Road",
    "address line 2": "Edmonton",
    "name": "Bayleaf",
    "outcode": "N9",
    "postcode": "8JE",
    "rating": 5,
    "type_of_food": "Curry"
  },
  {
    "URL": "http://www.just-eat.co.uk/restaurants-bayleafn9/menu",
    "_id": "55f14313c7447c3da705224a",
    "address": "61 Bounces Road",
    "address line 2": "Edmonton",
    "name": "Bayleaf",
    "outcode": "N9",
    "postcode": "8JE",
    "rating": 5,
    "type_of_food": "Curry"
  },
  {
    "URL": "http://www.just-eat.co.uk/restaurants-bayleaf-de75/menu",
    "_id": "55f14313c7447c3da705224b",
    "address": "39 Market Street",
    "address line 2": "Heanor",
    "name": "Bayleaf",
    "outcode": "DE75",
    "postcode": "7NR",
    "rating": 5,
    "type_of_food": "Curry"
  },
  .
  .
  .
```

This is an example output, to get the full output, test it locally.

```bash
curl localhost:8080/api/v1/restaurant/55f14313c7447c3da705224b | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   241  100   241    0     0    317      0 --:--:-- --:--:-- --:--:--   317
[
  {
    "URL": "http://www.just-eat.co.uk/restaurants-bayleaf-de75/menu",
    "_id": "55f14313c7447c3da705224b",
    "address": "39 Market Street",
    "address line 2": "Heanor",
    "name": "Bayleaf",
    "outcode": "DE75",
    "postcode": "7NR",
    "rating": 5,
    "type_of_food": "Curry"
  }
]
```

## The challenge starts here

Start by **adding a `SOLUTIONS.md` file justifying your responses.**

### Challenge 1. The API returns a list instead of an object

As you can see, the API returns a list in the two exposed endpoints:

- `/api/v1/restaurant`: Returns a list containing all the restaurants.
- `/api/v1/restaurant/{id}`: Returns a list with a single restaurant that match the `id` path parameter.

We want to fix the second endpoint. Return a json object instead of a json array if there is a match or a http 204 status code if no match found.

### Challenge 2. Test the application in any cicd system

![CICD](./assets/cicd.logo.jpg)

As a good devops engineer, you know the advantages of running tasks in an automated way. There are some cicd systems that can be used to make it happen.
Choose one, travis-ci, gitlab-ci, circleci... whatever you want. Give us a successful pipeline.

### Challenge 3. Dockerize the APP

![DockerPython](./assets/docker.python.png)

What about containers? As this moment *(2018)*, containers are a standard in order to deploy applications *(cloud or in on-premise systems)*. So the challenge is to build the smaller image you can. Write a good Dockerfile :)

### Challenge 4. Dockerize the database

![DockerMongo](./assets/docker.mongo.png)

We need to have a mongodb database to make this application run. So, we need a mongodb container with some data. Please, use the [restaurant](./data/restaurant.json) dataset to load the mongodb collection before running the application.

The loaded mongodb collection must be named: `restaurant`.

### Challenge 5. Docker Compose it

![Docker Compose](./assets/docker.compose.logo.png)

Once you've got dockerized all the API components *(python app and database)*, you are ready to make a docker-compose file.
**KISS**.

### Final Challenge. Deploy it on kubernetes

![Kubernetes](./assets/kubernetes.logo.png)

If you are a container hero, an excellent devops... We want to see your expertise. Use a kubernetes system to deploy the `API`. We recommend you to use tools like [minikube](https://kubernetes.io/docs/setup/minikube/) or [microk8s](https://microk8s.io/).

Write the deployment file *(yaml file)* used to deploy your `API` *(python app and mongodb)*.
