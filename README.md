# Django Chat App
## _Developed By Talha Umer_

The Django chat application was developed using Python Django Framework, PostgreSQL, and Django-channel.
# Features #
* Django 3.1.7
* Django Channels
* Uses PIP for python package management
* PostgreSQL database

## Functionalities

- Sign up functionality
- Log out functionality
- Log in functionality
- Show list of rooms
- Room detail view
- Creating a consumer
- Joining a chat
- Sending messages
- Storing messages

## OverView

This application was developed using the Django framework; I used Django channels for live chat functionality. Channels wrap Django’s native asynchronous view support, allowing Django projects to handle HTTP and protocols that require long-running connections.
This Django project has been divided into two portions; one is the user app which deals with user registration, signup, and logout functionality. The second app deals with messaging and WebSockets.
I need to create something called a "consumer for live traffic." The consumer will handle web socket traffic. Then I had to develop WebSockets with javascript, which sends the message to the backend where the message is stored in the database and returned to the screen for view. 

## Data Flow
When someone writes a message, go to the backend for storage and future view. We call the sync method for storing and async for the response at the backend. It works together with a sync wait for the storage of the message, and then it calls and replies to the front end. 
In that mechanism, all things are synchronized with no need for refreshing api. After some time, it automatically syncs new data and populates in the front. 

# Pre requisites #

* Install Python 3.9.5 if not previously installed (for ubuntu 18.04).  
```
$ sudo apt-get update
$ sudo add-apt-repository ppa:jonathonf/python-3.9.5
$ sudo apt-get update
$ sudo apt-get install python3.9.5
```
* Install PostgreSQL if not previously installed.  
```
sudo apt update
sudo apt install -y postgresql postgresql-contrib
```

* Install Python Package Index Tool pip3  
`sudo apt-get -y install python3-pip`

* Install virtual environment wrapper  
(further info found here: [https://linoxide.com/how-to-create-python-virtual-environment-on-ubuntu-20-04/](https://linoxide.com/how-to-create-python-virtual-environment-on-ubuntu-20-04/))
`$ apt-get install python3-venv`  

* Create directory for development, name it anything.
```
$ mkdir DjangoChatApp
$ cd DjangoChatApp
```


* When inside the directory create virtual environment, called env in example. Then activate the environment.  
```
$ virtual --python=python3.9.5 env
	virtualenv -p python3.9.5 env
	navigate into bin folder and run source activate
$ .env/bin/activate
```  
# Installation #

1. Enter CSPRO directory for development where project files stored.  
` (env) $ cd DjangoChatApp`
2. Install requirements  
`pip install -r requirment.txt`

3. Set up PostgreSql
Switch over to the mysql account by typing:  
```
$ sudo -u postgres psql
$ sudo -u postgres createuser —interactive
$ ALTER USER postgres WITH PASSWORD 'postgres';
$ create database database_name;
``` 

4. RUN Admin site migrations and other django app migrations.  
	'python manage.py migrate'

5. Run the server
`python manage.py runserver`

This should run the server and give an IP address that when entered into a web browser will bring up the development server. Address of the server is your IP address
most likely http://127.0.0.1:8000/.

6. Create superuser 
` python manage.py createsuperuser`
username: admin
email: superadmin@yopmial.com
username
password: xxxxxxxxx
this super admin will create when dependencies.sh runs

