# Coding Challenge
This repository contains a coding challenge introduced. The objective of this project is to create a GraphQL API using OMDB's API, following best practices and adhering to the SOLID MVC design pattern.


## Table of content

# Table of Contents

1. [Project Design](#project-design)
2. [Crawler and Core](#crawler-and-core)
3. [OMDB API and Authentication](#omdb-api-and-authentication)
4. [MVC Design Pattern](#mvc-design-pattern)
5. [Logging](#logging)
6. [Database Usage](#database-usage)
7. [GraphQL Features](#graphql-features)
8. [Error Handling and API Documentation](#error-handling-and-api-documentation)



## Project Design
The file design.drawio provides a basic design pattern implementation for this project. You can open it using draw.io. Please note that Figma is not supported.
Running the Service
To run the service, navigate to the src directory and execute the following command:
```bash
make deploy
```
Alternatively, you can run the tests by executing:

```bash 
make test
```
If you prefer using Docker, you can build and run the service using the following commands:

```bash
docker-compose build
docker-compose up -d
```

## Crawler and Core
Each crawler can have a core, ensuring a solid architecture. The design and structure of each core are identical, providing consistent behavior. A request session should interact with databases.

## OMDB API and Authentication
OMDB uses API key authorization, passing it as a parameter in the URL. Therefore, the project has adopted the necessary authentication for OMDB accordingly.

## MVC Design Pattern
The MVC (Model-View-Controller) design pattern was chosen for this project due to its suitability. The project includes models, controllers, and views. The model acts as the API interface retriever, responsible for generating data.

-   Pydantic models were used to validate the response data.
-   Exceptions were implemented to handle errors.


## Logging
No logger has been included in this repository to avoid overengineering for this phase. However, if the project were to be moved into production, it is recommended to implement a logger to track errors from both the API and the application's interface. This helps monitor the application's performance and errors.

## Database Usage
This repository does not require any kind of database as the data comes from another database and website. Storing the data is unnecessary since the existing dataset is large and continuously updated. Retrieving and displaying the data to end-users is more efficient in this scenario.

## GraphQL Features
The GraphQL implementation includes the skip and limit features, allowing retrieval of multiple objects. Asynchronous requests using the HTTPX client fetch all pages simultaneously. The first page is fetched initially to determine if additional pages need to be retrieved. This approach ensures consistent response times, regardless of the number of items requested. However, requesting an excessively large number of items may lead to API timeouts. It is recommended to avoid exceeding 100 pages.

## Error Handling and API Documentation
Due to the lack of proper documentation such as Redocs or Swagger for the OMDB API, unexpected responses could not be anticipated, however the project includes error handling to handle API responses accordingly to what I encountered during the development.


Thank you for your interest in this coding challenge! If you have any further questions, please feel free to reach out :)
Ah, I just learned about graphene, and I uploaded my dirty playground as well in MVP :D
