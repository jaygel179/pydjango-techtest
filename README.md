Assignar Python/Django Tech Test
================================

This is a base project for technical tests we use in our hiring process.

The actual technical tasks and challenges are not included in this repo 
so that we are able to customise the tasks/challenges according to the 
roles we are looking for.    


Setup
-----

### Installation

This project is a very minimal Python setup. You are free to set 
it up locally in your own way (`virtualenv`, `venv`, `pyenv`, `poetry`, 
Docker, etc.). 

### Database setup

Setup your initial database (SQLite) using the following command.
    
    $ ./manage.py migrate
    
Create your first superuser using the following command.

    $ ./manage.py createsuperuser

### Running the server

    $ ./manage.py runserver
