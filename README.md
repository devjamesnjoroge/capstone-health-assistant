#### HEALTH ASSISTENTE

`By devjamesnjoroge`

### Description
This is a web app where a user can create a profile and add health information. They are also able to create posts and see other users health related posts.

### Features
- Create a profile
- Add medical history
- Add diet information
- Create posts
- See other users posts
- See other users profile

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/devjamesnjoroge/capstone-health-assistant/
```
##### Navigate into the folder and install requirements  
 ```bash 
cd medical 
```
##### Install and activate Virtual  
 ```bash 
- pipenv shell
```  
##### Install Dependencies  
 ```bash 
 pipenv install requests
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations community
 ``` 
 Now Migrate  
 ```bash 
 make migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 make test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
- [Python](https://www.python.org/)  
- [Django](https://docs.djangoproject.com/en/2.2/)  
- [Heroku](https://heroku.com)  

## Contact Information   


-   Email- [James Njoroge](mailto:developerjaymmy@gmail.com)
-   Linkedin - [James Njoroge](https://www.linkedin.com/in/devjamesnjoroge/)

## License 

* *MIT License:*
* Copyright (c) 2022 **James Njoroge**

[Go Back to the top](#HEALTH)