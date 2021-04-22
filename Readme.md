# RabbitMQ Projects

## Install Packages

    $ git clone git@github.com:rajuu89/rabbitmq_codetest.git
    $ cd Python-RabbitMQ
    $ pip3 install -r requirements.txt

## Configure app

    Copy `.env.sample` file into `.env` and update the envirment variables

## Running the project

  Open a terminal run the following commands
    $ python scripts/migrations.py
    $ python scripts/consumer.py

  Open another terminal run the following commands
    $ python scripts/producer.py
