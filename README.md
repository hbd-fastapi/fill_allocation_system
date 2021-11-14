# FILL ALLOCATION SYSTEM
> This is fill allocations system based on microservices written and fastapi and dockerized. The idea is to spread incoming fills accoridingly to given percentages.

## Table of Contents
- [FILL ALLOCATION SYSTEM](#fill-allocation-system)
  - [Table of Contents](#table-of-contents)
  - [Initial requirements](#initial-requirements)
  - [General Information](#general-information)
  - [Schema](#schema)
  - [Technologies Used](#technologies-used)
  - [Setup](#setup)
  - [Room for Improvement](#room-for-improvement)
  - [Acknowledgements](#acknowledgements)


## Initial requirements
- [x] - runnable from localhost
- [x] - no persistance needed
- [x] - fastapi in python
- [x] - production ready
- [x] - published on github

## General Information
- Applications consists of 4 microservices:
  - AUM Server
  - Fill Server
  - Controller Server
  - Position Server
- All of them communicate with each other to provide payload, process the data and print out new positions at the end

## Schema
![Application Schema](https://github.com/hbd-fastapi/fill_allocation_system/blob/master/schema.png?raw=true "Schema")

## Technologies Used
- Docker - version 3.8
- Python - version 3.8.10
- fastapi - version 0.70.0

## Setup
To compose application you need docker installed and then you can:
`
docker-compose up --build
`

## Room for Improvement
Room for improvement:
- Adding more unittests
- Improve logging to remove readability
- Refactor and improve logic for spreading the fills

## Acknowledgements
- The shape of the readme file was inspired by [this website](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
- The content of the Dockerfiles was inspired by [this website](https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8)
- Some solutions applied in this project were inspired by those 2 repos (especially for configuring docker):
  - [rmisiarek repo](https://github.com/rmisiarek/fill_allocation_system)
  - [zak44h repo](https://github.com/zak44h/fill-allocation-system)

