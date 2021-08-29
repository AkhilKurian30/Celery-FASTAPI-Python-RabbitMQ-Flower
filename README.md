Description

Purpose : Queue Rest API Calls which take long time to process

This is a basic implementation of the Python FAST API app with celery and RabbitMQ, Flower as tracking dashboard




#Start application

Run application as we run normal FAstApi Application

    python3 -m venv v

    source v/bin/activate

    pip install -r package.txt
    
    python run.py

#Start Celery worker in other terminal

    celery -A tasks worker

#Start Flower monitoring dashboard in other terminal
    celery flower -A worker --broker:pyamqp://guest@localhost

    http://127.0.0.1:5555/tasks => for flowe dashboard

    

#Queuing system used 
    RabbitMQ



Install RabbitMQ in windows :

Download and install ERlang http://erlang.org/download/otp_win64_22.3.exe

Downlaod and install RabbitMQ https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.8/rabbitmq-server-3.8.8.exe

Go to RabbitMQ Server install Directory C:\Program Files\RabbitMQ Server\rabbitmq_server-3.8.3\sbin

Run command rabbitmq-plugins enable rabbitmq_management

Open browser and enter http://localhost:15672/ to redirect to RabbitMQ Dashboard

Also we can Open it with IP Address http://127.0.0.1:15672

Login page default username and password is guest

After successfully login you should see RabbitMQ Home page

Install RabbitMQ in Linux : https://www.youtube.com/watch?v=eazz-Je4HAA

su - root

password : 

bash

sudo apt-get update

sudo apt-get install erlang

sudo apt-get install rabbitmq-server

sudo systemctl enable rabbitmq-server

sudo systemctl start  rabbitmq-server

sudo systemctl status  rabbitmq-server

sudo rabbitmq-plugins enable rabbitmq_management

best explanation :: https://www.cloudamqp.com/blog/part1-rabbitmq-for-beginners-what-is-rabbitmq.html