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

Setup your initial database (SQLite).

    $ ./manage.py migrate

Create your first superuser.

    $ ./manage.py createsuperuser

Load initial seed data.

    $ ./manage.py loaddata images

Development
-----------

### Running the server

    $ ./manage.py runserver


### Running test case

    $ ./manage.py test


Project Information
-------------------

This is a Django example project (`imagedb`) that includes one Django
app called `images`.

The `images` app uses two models, `Image` and `ImageLabel`.

* `Image` - refers to an image that you can upload/download.
* `ImageLabel` - refers to a label of an object inside the image.

An `Image` can have multiple `ImageLabel`s. An `ImageLabel` belongs to
only one `Image`.

A basic Django admin page is available at http://localhost:8000/admin.



Tech Test Details
-----------------

### Setup AWS Credentials Environment Varialbes
```
export AWS_ACCESS_KEY=<access_key>
export AWS_SECRET_KEY=<secret_key>
export AWS_REGION=<region_name>
export AWS_BUCKET_NAME=<bucket_name>
```

### Urls

#### Image View
- list all images - `<path>/images`
- view specific image - `<path>/images/<image_id>`

#### ImageLabel View
- list all image labels - `<path>/imagelabels`
- view specific image labels - `<path>/imagelabels/<imagelabel_id>`


From the image list view you can upload image using the upload button.
