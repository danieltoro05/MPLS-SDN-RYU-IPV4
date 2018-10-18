#!/bin/bash
# MPLSconfig.sh
# Setting router IP addresses using the REST API
##### Addresses for router s1 #####
# Network 1
curl -X POST -d '{"address":"10.0.1.100/24"}' http://localhost:8080/router/0000000000000001
##### Addresses for router s2 #####
# Network 2
curl -X POST -d '{"address":"10.0.2.100/24"}' http://localhost:8080/router/0000000000000002
##### Addresses for router s3 #####
# Network 3
curl -X POST -d '{"address":"10.0.3.100/24"}' http://localhost:8080/router/0000000000000003
##### Prefix mapping for router s1 #####
curl -X POST -d '{"prefix":"10.0.2.0/24", "port":"3"}' http://localhost:8080/router/0000000000000001
curl -X POST -d '{"prefix":"10.0.3.0/24", "port":"3"}' http://localhost:8080/router/0000000000000001
##### Prefix mapping for router s2 #####
curl -X POST -d '{"prefix":"10.0.1.0/24", "port":"4"}' http://localhost:8080/router/0000000000000002
curl -X POST -d '{"prefix":"10.0.3.0/24", "port":"4"}' http://localhost:8080/router/0000000000000002
##### Prefix mapping for router s3 #####
curl -X POST -d '{"prefix":"10.0.1.0/24", "port":"3"}' http://localhost:8080/router/0000000000000003
curl -X POST -d '{"prefix":"10.0.2.0/24", "port":"3"}' http://localhost:8080/router/0000000000000003
##### Prefix mapping for router s4 #####
curl -X POST -d '{"prefix":"10.0.1.0/24", "port":"1"}' http://localhost:8080/router/0000000000000004
curl -X POST -d '{"prefix":"10.0.2.0/24", "port":"2"}' http://localhost:8080/router/0000000000000004
curl -X POST -d '{"prefix":"10.0.3.0/24", "port":"3"}' http://localhost:8080/router/0000000000000004
##### Setting router s4 as LSR #####
curl -X POST -d '{"router":"lsr"}' http://localhost:8080/router/0000000000000004
