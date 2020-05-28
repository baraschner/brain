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
 The client is responsible for uploading snapshots to the server. The client exposes the following cli and api
 ```python
from brain.client import upload_sample

upload_sample(file,host,port,test)
```
```shell script
python -m cortex.client upload-sample \
      --host '127.0.0.1'             \
      -port 8000                    \
      'snapshot.mind.gz'

```
 

