# pyRedisExample

Here is a very simple example for running Redis in a Docker container and accessing that conainer from another Docker container running Python.

## Getting Started

This repository was tested on Docker CE Version 18.06.1-ce-win73 (19507) on a Windows 10Pro machine. I am assuming some familiarity with Docker and Docker Compose although no in-depth knowledge of either is required. The Python code has been stripped dwn to the bare essentials so you get an idea of the code you need to write in order to have Python store and retrieve key/value pairs in Redis.

### Prerequisites

The only prerequisite is Docker which comes with Docker Compose. Here are the links to the Docker pages  for the most popular operating systems.

[Windows](https://docs.docker.com/docker-for-windows/) \
[MAC](https://docs.docker.com/docker-for-mac/)  \
[Linux - Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)  \
[Other Opereating Systems](https://docs.docker.com/install/overview/)


### Installing

Clone the repository to yout machine. Open a terminal window in the directory where the docker-compose.yml file is located. After that all you need to do to create the containers is type:

docker-compose up --build

## Function

Docker Compose will start 2 containers. One will be a Redis container. If you aren't familiar with [Redis](https://redis.io/) it is an in-memory key/value store. The Redis container can be refernced over the network at a port you expose. In this case I am using the deault port of 6379. This can be changed in the redis.conf file. The second container has Python installed. Once the Python container is running a simple Python app will be run to test the connectivity with the Redis container. After that app completes the Python container will terminate but the Redis container will remain running.

If you wish to keep the Python container running so you can open a terminal into that container then you need to remove the following line from the ./python/
dckerfile

CMD [ "python", "/usr/local/etc/redistest.py" ]

Since this is just a simple example, the Python app  doesn't do much but store a couple of simple key/value pairs and retrieve them. You should check the Redis documentation for storing more complex structures in Redis. 