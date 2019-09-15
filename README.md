# vtb_hack
web service for the joint approval of new documents and projects


[Server] Python (Flask)

[Client] Vue

[Database] PostgreSQL

[Deployment] Docker


## Getting Started

#### Install npm
```
brew install yarn
```

#### Install docker

```
https://docs.docker.com/compose/install/
```

## Build and Run

```
git clone https://github.com/AndreiSukharev/diversity_hack.git diversity_hack
cd vtb_hack
docker-compose up --build
cd client
yarn install
yarn dev
front: http://localhost:5000
server: http://localhost:4440/ 
```
#### Test

Create test users:
```
docker exec flask bash -c "python test_entity.py"
```

#### Note Docker

Run postgres client:

```
docker exec -it postgres psql matchaDB user
```
Enter in container:
```
docker exec -it flask bash
```
Remove all:
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```
