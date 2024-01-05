# LAB 4: Programming RESTful APIs

This repository contains a Flask application consisting of NASA blog where the user can register, login, see the APOD image of the day and introduce some coordinates and date to see a satellite picture. 

#### The application uses docker compose and it has 4 services running in different containers: 
- MySQL
- Gateway
- APOD
- Auth

![NASA Blog](/src/gateway/static/images/nasa_blog_image.png)

Run the following command to start the application:
```
docker-compose up --build
```
