#  YaMDb

## Description
The YaMDb project collects user feedback on works. The works themselves are not stored in YaMDb, you can't watch a movie or listen to music here.
The works are divided into categories, and a genre can also be assigned from the list of preset ones.
Only the administrator can add works, categories and genres.
Grateful or indignant users leave text reviews for the works and put
product score in the range from one to ten (integer); from user ratings
an average assessment of the work is formed - rating. For one work, the user can leave only one review.

## Input data
This project was carried out in several stages:
1. Writing the service itself based on the terms of reference. It was carried out jointly with two other developers. I was in charge of genres, categories and titles.
You can see the finished part and try it on a local machine [here](https://github.com/Oleg-2006/api_yamdb).
2. Configuring application separation by Docker-Compose containers. 
3. Connecting GitHub Actions with the setting:
    * automatically run tests
    * building and updating images on Docker Hub
    * deploy the project to the server

## Technologies used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=for-the-badge&logo=Docker&logoColor=white&color=008080) ![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=for-the-badge&logo=Docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Action status](https://github.com/Oleg-2006/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## YaMDb API resources
- Resource **auth**: authentication.
- Resource **users**: users.
- Resource **titles**: works to which they write reviews (a certain movie, book or song).
- Resource **categories**: categories (types) of works ("Films", "Books", "Music").
- Resource **genres**: genres of works. One work can be tied to several genres.
- Resource **reviews**: reviews of works. The review is tied to a specific product.
- Resource **comments**: comments on reviews. The comment is tied to a specific review.

## User roles and permissions
- **Anonymous** - can view descriptions of works, read reviews and comments.
- **Authenticated user** (user) - can read everything, like Anonymous, can post reviews
  and rate works, can comment on reviews; can edit
  and delete your reviews and comments, edit your ratings of works. This role is assigned
  by default for every new user.
- **Moderator** (moderator) - the same rights as the Authenticated user,
  plus the right to remove and edit any reviews and comments.
- **Administrator** (admin) — full rights to manage all project content.
  Can create and delete works, categories and genres. Can assign roles to users.
- **Django Superuser** has administrator rights, a user with admin rights.

## Preparing and launching the project
### Clone the repository
Clone the repository to your local machine:
```bash
git clone git@github.com:Oleg-2006/yamdb_final.git
```

### Installation on a remote server (Ubuntu):
**Step 1** Log in to your remote server
Before you get started, you need to log in to your remote server:
```bash
ssh <USERNAME>@<IP_ADDRESS>
```

**Step 2** Install docker on the server:
Enter the command:
```bash
sudo apt install docker.io 
```

**Step 3** Install docker-compose on the server:
Enter commands:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

**Step 4** Copy the prepared files:
Copy the prepared files `docker-compose.yaml` and `nginx/default.conf` from your project to the server in `home/<your_username>/docker-compose.yaml` and `home/<your_username>/nginx/default.conf ` respectively.
Enter the command from the root folder of the project:
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp -r nginx/ <username>@<host>:/home/<username>/
```

**Step 5** Add Secrets:
To work with Workflow, add environment variables to Secrets GitHub for work:
```bash
SECRET_KEY=<SECRET_KEY>  # after changing setting.py
DEBUG=<True/False>  # after changing setting.py
ALLOWED_HOSTS=<hosts>  # after changing setting.py
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DOCKER_PASSWORD=<password DockerHub>
DOCKER_USERNAME=<username DockerHub>
USER=<username to connect to the server>
HOST=<IP server>
PASSPHRASE=<password for the server, if set>
SSH_KEY=<your SSH key (to get the command: cat ~/.ssh/id_rsa)>
TELEGRAM_TO=<ID of your telegram account>
TELEGRAM_TOKEN=<your bot token>
```

**Step 6** To start the workflow, you need to start the project:
```bash
git add .
git commit -m "your comment"
git push
```
After the push, all the items described in `yamdb_workflow.yml` will be executed
**Workflow** consists of four steps:
- **tests**
  Checking the code for compliance with PEP8, automatically running tests.
- **build and push Docker image to Docker Hub**
  Building and publishing the image on DockerHub.
- **deploy**
  Automatic deployment to the combat server.
  The project deployment instructions are described in the `docker-compose.yaml` file.
  The project is deployed in three containers:
  - *db* database container via postgres:13.0-alpine
  - *web* Django app container
  - *nginx* container responsible for distributing statics
- **send_massage**
  Sending a notification to a telegram chat.

**Step 7** After a successful deployment:
Go to the combat server and run the commands (only after the first deployment):
##### Create and apply migrations:
```bash
sudo docker-compose exec web python manage.py makemigrations --noinput
sudo docker-compose exec web python manage.py migrate --noinput
```
##### Loading statics
```bash
sudo docker-compose exec web python manage.py collectstatic --no-input 
```
##### Create a Django superuser:
```bash
sudo docker-compose exec web python manage.py createsuperuser
```

**Step 8** Project started
The project will be available at your IP address.

## Programs for sending requests

* API testing via httpie - API console client.
If you like this console API client, [you can find installation instructions there, on the developers' website.](https://httpie.io/docs/cli/installation)

* API Testing with VS Code Extension
The extension [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) allows you to send HTTP requests directly from VS Code and view responses to them in the same interface.

* API Testing with Postman
Postman is a popular and convenient API client that can send requests and show responses, save request history and authentication data, and allow you to design and test API.
[Download Postman from the download page](https://www.postman.com/downloads/) project and install it on your work machine.

## Document examples:

`api/v1/categories/` (GET, POST, DELETE): get, create or delete a categories
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```
`api/v1/genres/` (GET, POST, DELETE): get, create or delete a genres
```
[
  {
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "name": "string",
      "slug": "string"
    }
  ]
  }
]
```
`api/v1/titles/` (GET, POST, PUTCH, DELETE): get, create, update or delete a titles
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
            {
              "name": "string",
              "slug": "string"
            }
          ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```

## Request examples
Examples of requests, access rights, possible answers are available in the [documentation](http://127.0.0.1:8000/redoc/) attached to the project

## Authors
- [Aleh Maslau](https://github.com/Oleg-2006)
