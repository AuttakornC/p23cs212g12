# Flash Card
## Start Web Application
* **Clone** this project to your local disk & get in that folder.
* **Install Python & Requirements Libraries** by run this command.
```bash
pip install -r requirements.txt
```
**OR** if you have **pipenv** use this command.
```bash
pipenv install -r requirements.txt
```
* Give permission to run execute file
```bash
chmod +x gunicorn_starter.sh
```
* **Install Docker**.
* **Run this command** to start project.
```bash
docker compose up
```
**docker compose** : it'll start to create **Database Docker Container (Postgres)** and then build our **Flask Application** on **http://localhost:56734/ (config port in compose.yml file)**, all containers will run on the same network.
## Devolopment
network on docker may change container's IP. For the application can connect to the database correctly, you should check about ip address of database container. Following this step.
* **run network inspect command on docker**
```bash
docker network inspect <NETWORK_NAME>
```
you can list your network name by this command.
```bash
docker network ls
```
our compose network will include the name that in **compose.yml** on bottom of the file under **networks:**.
* **After that** look for key **Containers** look at the **IPv4Address** of **"bananachoco-db-1"**. you must use it in **database config (host)** in backend code.
```json
"Containers": {
    "868ff5b615b9ebee6f9f0136b29a9076654bc248a610a45a65b747c07047fed1": {
        "Name": "bananachoco-db-1",
        "EndpointID": "1cfc5df7c3ef25dec5dbbeff5ef38f480d02a802e43552d56811c42149bbe3ab",
        "MacAddress": "02:42:ac:12:00:02",
        "IPv4Address": "172.18.0.2/16",
        "IPv6Address": ""
    },
        "ab3b5fc3cc1f77f8505b94d39d76fc5f36872393b7cc7e305c0167e9575f7822": {
        "Name": "bananachoco-server-1",
        "EndpointID": "40bbf6279a94b030f5b8beaf92b806d876e8e790c4aaffc105e2e043fbd67407",
        "MacAddress": "02:42:ac:12:00:03",
        "IPv4Address": "172.18.0.3/16",
        "IPv6Address": ""
    }
},
```