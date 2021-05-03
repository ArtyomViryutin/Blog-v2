# Blog_v2

Simple Blog implementation in Django

## Features
1) Django
2) PostgreSQL
3) Celery
4) Redis
5) Flower

## Installation

1) `git clone https://github.com/ArtyomViryutin/Blog_v2.git`


2) In the project folder create `.env.dev` file and set up following variables:

    **Django settings**
    
    `SECRET_KEY=<Your SECRET_KEY>`
    
    `DEBUG=<0 or 1>`
    
    `ALLOWED_HOSTS=<e.g. localhost 127.0.0.1>`
    
    **Database settings**
    
    `DATABASE_ENGINE=django.db.backends.postgresql`
    
    `DATABASE_NAME=postgres`
    
    `DATABASE_USER=postgres`
    
    `DATABASE_PASSWORD=postgres`
    
    `DATABASE_HOST=db`
    
    `DATABASE_PORT=5432`
    
    **SMTP settings**
    
    `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
    
    `EMAIL_USE_TLS=1`
    
    `EMAIL_HOST=smtp.gmail.com`
    
    `EMAIL_PORT=587`
    
    `EMAIL_HOST_USER=<Your gmail email>`
    
    `EMAIL_HOST_PASSWORD=<Your gmail password>`
    
    `DEFAULT_FROM_EMAIL=<Your gmail email>`
    
    **Celery settings**
    
    `CELERY_BROKER_URL=redis://redis:6379`


3) `$ docker-compose up --build`

## Usage
### Blog
1) _http://localhost:8000/_
2) _http://127.0.0.1:8000/_
3) _Your own_

### Flower
1) _http://localhost:5555/_

2) _http://127.0.0.1:5555/_



