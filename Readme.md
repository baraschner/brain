Brain Computer Interface
[![Build Status](https://travis-ci.org/baraschner/brain.svg?branch=master)](https://travis-ci.org/baraschner/brain)
[![codecov](https://codecov.io/gh/baraschner/brain/branch/master/graph/badge.svg)](https://codecov.io/gh/baraschner/brain)
[![Documentation Status](https://readthedocs.org/projects/baraschnerbrain/badge/?version=latest)](https://baraschnerbrain.readthedocs.io/en/latest/?badge=latest)

# Brain
The  project includes a client, which streams cognition snapshots to a server, which then publishes them to a message queue, where multiple parsers read the snapshot, parse various parts of it, and publish the parsed results, which are then saved to a database.
The results are then exposed via a RESTful API, which is consumed by a CLI; there's also a GUI, which visualizes the results in various ways.

# Install
1. Clone the repository.
2. Run ``` ./scripts/install.sh ```
3. Activate the virtual environment.
4. Run the tests by using  ```pytest```

#Deployment
The project is deployable with docker. We assume that docker is already installed.
To deploy the project (which deploys the server, parsers, api, ui) use
 ```./scripts/run-pipeline.sh```.
 
 #Project Components
 ## Client
 The client is responsible for uploading snapshots to the server. The client exposes the following cli and api:
 ```python
from brain.client import upload_sample

upload_sample(file,host,port,test)
```
```shell script
python -m cortex.client upload-sample \
      --host '127.0.0.1'             \
      --port 8000                    \
      'snapshot.mind.gz'
```
The default host is 127.0.0.1 and the default port is 8000.
 
 ## Message Queue
 The system uses RabbitMQ for communication between the server and the parsers and between the parsers and the the saver.
 ## Server
 The server is responsible for receiving snapshots from the client the pass them to the queue.
 The server exposes the following cli and api:
  ```python
from cortex.server import run_server
def print_message(message):
    print(message)
run_server(host='127.0.0.1', port=8000, publish=print_message)
```
```shell script
python -m cortex.server run-server \
      --host '127.0.0.1'          \
      --port 8000                 \
      'rabbitmq://127.0.0.1:5672/'
```
127.0.0.1:8000 is the default address to which the server binds.

##Parsers
The parsers are simple functions or classes, built on top of an aspect-oriented platform. They are easily deployable as microservices consuming raw data from the queue, and producing parsed results to it. The parsers have the following api and cli:
```python
from brain.parsers import run_parser
data = … 
result = run_parser('pose', data)
```
```shell script
python -m cortex.parsers parse 'pose' 'snapshot.raw' > 'pose.result'
```
```shell script
python -m cortex.parsers run-parser 'pose' --queue 'rabbitmq://127.0.0.1:5672'
```
The default queue url is ```'rabbitmq://127.0.0.1:5672'```.
Creating new parsers is easy. A parser is either:
- A function that has a ``field`` property.
- A class that has a ```field``` property and a ```parse``` function. The constructor of the class must contain no arguments.

To add a new parser just add a module that contains one of the above parser options in the ```brain/parsers/fields``` directory.
The following parsers exist by default:
- pose
- colorImage
- depthImage
- feelings
- user

##Database
The system uses MongoDB us the database.

## Saver
The saver saves parsed results to the MongoDB database. The saver exposes the following cli and api:
```python
from brain.saver import Saver
saver = Saver(database_url)
data = …
saver.save('pose', data)
```
```shell script
python -m cortex.saver save                     \
      --database 'postgresql://127.0.0.1:5432' \
     'pose'                                       \
     'pose.result' 
```

```shell script
python -m cortex.saver run-saver  \
      --database 'mongodb://127.0.0.1:5432' \
      --queue 'rabbitmq://127.0.0.1:5672/'
```

##The API
The API server consumes the database. It has the following endpoints:
- ```/users```
Returns the list of all the supported users, including their IDs and names only.
- ```/users/user-id```
Returns the specified user's details: ID, name, birthday and gender.
- ```/users/user-id/snapshots```
Returns the list of the specified user's snapshot IDs and datetimes only.
- ```/users/<user-id/all/field_name ```
Returns all the results in the field ``field_name`` over all snapshots of the given user.

- ```/users/user-id/snapshots/snapshot-id```
Returns the specified snapshot's details: ID, datetime, and the available results' names only (e.g. pose).

- ```/users/user-id/snapshots/snapshot-id/field-name```
Returns the specified snapshot's result in a reasonable format. You should support pose, color-image, depth-image and feelings, where anything that has large binary data should contain metadata only, with its data being available via some dedicated URL (that should be mentioned in its metadata), like so:
    - ```/users/user-id/snapshots/snapshot-id/colorImage/data``` 

```python
from cortex.api import run_api_server
run_api_server(
    host = '127.0.0.1',
    port = 5000,
    database_url = 'postgresql://127.0.0.1:5432')
```

```shell script
python -m cortex.api run-server \
      --host '127.0.0.1'       \
      --port 5000              \
      --database 'mongodb://127.0.0.1:5432'
```

## The CLI
The cli provides functions that consume the api. For example
```shell script
python -m brain.cli get-users
python -m brain.cli get-user 1
python -m brain.cli get-snapshots 1
python -m brain.cli get-snapshot 1 2
python -m brain.cli get-result 1 2 'pose'
```
One may get all available CLI functions using ```python -m brain.cli -h```.

## The UI
The user interface server provides a GUI that allows navigation through the data in the snapshots in the system.
The UI has two components.
- A simple web server written using Flask.
- The (client side) GUI application written using react.

By design, in order to make the UI efficient the one's that consume the API are
 actually the clients.
 The UI server has the following api and cli:
 ```python
from brain.ui import run_server
run_server(
    host = '127.0.0.1',
    port = 8080,
    api = "127.0.0.1:5000"
... )
```

```shell script
python -m cortex.gui run-server 
      --host '127.0.0.1'       
      --port 8080              
      --api '127.0.0.1:5000'   
```
The reason the UI has to know the api address is in order to plant it in the template.
Then the clients will consume it.


