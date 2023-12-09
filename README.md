# Bigdata-pipeline
This is the repository for as1 Rmit BigData course. This guideline help you to walkthrough the process of setting up Docker containers for kafka and cassandra to create a data pipeline 

### Tools: 
* Python 3.10 
* Apache Kafka
* Window power shell
* ipython
* Docker
* Visual Studio Code

### APIS for assingment 
- OpenWheather API 
- Faker Api
- Mockaroo Api 

### Prerequisites
- Python 3.10 (actually just 3.7+)
- Docker for containerization 

### Installation and implementation guideline 
```bash
git clone https://github.com/namtoptall/bigdata-e2epipeline.git
cd .\bigdata-e2epipeline\
 ```

### add keys
- Go to owm-producer/openweathermap_service.cfg, change your token keys 

### guideline 
1. Create Kafka and Cassandra network 
```bash
    docker network create kafka-network
    docker network create cassandra-network
    docker network ls   # list network, check if it successfully 
```
2. run kafka and cassandra containers
```bash 
    docker-compose -f cassandra/docker-compose.yml up -d
    docker-compose -f kafka/docker-compose.yml up -d
    #check 
    docker ps -a    
``` 
3. Access Kafka UI frontend

- http://localhost:9000 (username: admin; password: bigbang)

- Add a data pipeline cluster:
    + Cluster Name: mycluster
    + Cluster Zookeeper: zookeeper:2181

- Enable the following options:
    + Enable JMX Polling
    + Poll consumer information
    + Enable Active OffsetCache Click Save.  

4. Go to the Kafka-connect container on Docker 
- run the following command: 
```bash
./start-and-wait.sh
```

5. Initialize Provider and Consumer for Kafka with 3 different APIs
```bash
# producer
docker-compose -f owm-producer/docker-compose.yml up -d
docker-compose -f faker-producer/docker-compose.yml up -d
docker-compose -f mockaroo-producer/docker-compose.yml up -d

# Consumer
docker-compose -f consumers/docker-compose.yml up -d
```
6. Open the cassandra-cli and check the data
```bash 
    docker exec -it cassandra bash 
    cqlsh --cqlversion = 3.4.4.127.0.0.1
    desc keyspaces;
    use kafkapipeline;
    show tables;
    # check the data
    select * from weatherreport;
    select * from fakerdata;
    select * from mockaroo;
```

7. Data Visualization
```bash
    docker-compose -f data-vis/docker-compose.yml up -d
```
8. shut down containers and network when done 
```bash    
docker-compose -f data-vis/docker-compose.yml down
docker-compose -f consumers/docker-compose.yml down
docker-compose -f owm-producer/docker-compose.yml down 
docker-compose -f kafka/docker-compose.yml down 
docker-compose -f cassandra/docker-compose.yml down 
docker network rm kafka-network
docker network rm cassandra-network
```

### Mockaroo api: 
1. Overview
Mockaroo offers two different approaches for downloading data programmatically:
2. Generate API
Mockaroo's Generate API is a single endpoint that you can use to generate data based on a saved schema or fields you define in the post body of the request. Anything you can generate via the website can also be generated via the data API.
3. Mock APIs
Mock APIs give your full control over URLs, handling request parameters, and simulating errors. Mock APIs are ideal for simulating back ends before they're built so you can start working on your front end code. Configure Mock APIs using the APIs link in the header.
* mockaroo data dictionary: 
- simple table with id,first_name,las_name,full name and age.

### data visulization : 
- Due to the time constraint, I just do simple visulization with plotting the temperature of the cities
