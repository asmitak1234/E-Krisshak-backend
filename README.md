<!-- Made by- Asmita Kumari -->

# E-Krisshak-backend
<!-- explaining setup,functionalities, and deployment steps. -->
<!-- ## for heading, # for main heading,following for links and lists ,[CONTRIBUTING.md](CONTRIBUTING.md) file for locating to file.-->


## Description

Hello Everyone, I am ASMITA KUMARI , a young learner and i am here with frontend part of my project called "E-Krisshak" , A farmer availability management system that helps to select and find a farmer for your field with their proper and detailed Personal, Professional and Contact information that helps you to store and choose them according to your requirements.This is a Secure and Efficient WebApp and I am making this project with the intension of helping the land-owners that can't find farmer for their field and many farmers that are seeking for work ,especially in INDIA.

This project is a full-stack CRUD(Create, Read, Update, Delete) Web Application using Django for the backend, React for the frontend, and MySQL as the database. This README provides instructions on setting up, using, and deploying the backend of this project.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Connection](#connection)
- [Functionalities](#functionalities)
- [Deployment](#deployment)

## Requirements

- Python 3.8 or higher
- Node.js 14 or higher
- npm (or yarn) for managing JavaScript packages
- MySQL server
- Other Requirements are in the file [requirements.txt](requirements.txt)

## Setup

### Backend Setup

1. *Clone the Repository*

   bash:
   git clone https://github.com/asmitak1234/E-Krisshak-backend.git
   cd E-Krisshak-backend
   

2. *Create and Activate a Virtual Environment*

   bash:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install Backend Dependencies*

   bash:
   pip install -r requirements.txt
   

4. *Configure the Database*

   - Create a MySQL database and user. Update the database settings in [ekrisshakbackend/settings.py](ekrisshakbackend/settings.py):

     python:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     

5. *Apply Migrations*

   bash:
   python manage.py migrate
   

6. *Create a Superuser*

   bash:
   python manage.py createsuperuser
   

7. *Run the Development Server*

   bash:
   python manage.py runserver

    The Django Backend development server will typically run on http://127.0.0.1:8000/.
   
Other Requirements are in the file [requirements.txt](requirements.txt)

### Frontend Setup

1. *Navigate to the Frontend Directory*

   bash:
   cd ekrisshakfrontend
   

2. *Install Frontend Dependencies*

   bash:
   npm install  # or yarn install
   

3. *Start the Development Server*

   bash:
   npm start  # or yarn start
   

   The frontend will typically run on http://localhost:3000.

## Connection 

- *Frontend-Backend*: Frontend and Backend is connected by Axios library.
- *Backend-Database*: Backend and Database is connected through mysqlclient by updating Database information in settings.py after creating database.
 
For Security reasons you can add .env file to protect your sensitive data from settings.py and including it in [.gitignore](.gitignore) file.

## Functionalities

- *User Authentication*: Users can register and log in to their profiles with alerts.
- *Responsive Design*: The frontend is designed to be responsive and dynamic that works on various devices.
- *Navigation*: Users can navigate to different web pages(Home , List , Manage) through Side Navigation Bar.
- *Form Handling*: User input and form submissions are handled with proper validation mechanisms.
- *CRUD Operations*: Perform create, read, update, and delete operations on the main resources.
- *API Integration*: The frontend communicates with the backend via a RESTful API.

## Deployment

   #### Overview
      This section describes the steps to deploy the backend of this project, which is built with Django, uses MySQL as its database, and utilizes python-decouple for managing environment variables, to Heroku. The frontend built with React is not covered here but will need to be deployed separately.

   #### Prerequisites

   Before deploying the backend, ensure you have the following:
   
   - A Heroku account (sign up at Heroku).
   - The Heroku CLI installed. You can install it by following Heroku CLI installation instructions.
   - MySQL database and user credentials.
   - Your Django project should be ready for deployment with a requirements.txt file and necessary configurations.

   #### Steps to Deploy

   1. *Prepare Your Django Project*

       - Install Required Packages

         Ensure you have gunicorn, dj-database-url, and python-decouple in your requirements.txt for running the app on Heroku.
         pip install gunicorn dj-database-url python-decouple

         Then, add these to your requirements.txt:
         pip freeze > requirements.txt

         Configure settings.py
         
         from decouple import config, Csv
         import dj_database_url

       - Load environment variables

         SECRET_KEY = config('DJANGO_SECRET_KEY')
         DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

       - Database configuration

         DATABASES = {
            'default': dj_database_url.parse(config('DATABASE_URL'))
         }

       - Allowed hosts

         ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
         Create a Procfile
         Create a Procfile in the root directory of your project to tell Heroku how to run your application:

         web: gunicorn myproject.wsgi

         Add Static File Configuration
         Install whitenoise to serve static files:

         pip install whitenoise
         Update your settings.py:
         MIDDLEWARE = [
            'whitenoise.middleware.WhiteNoiseMiddleware',
            # other middleware...
         ]

         STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

         Add whitenoise to requirements.txt:
         pip freeze > requirements.txt

   2. *Deploy to Heroku*

      - Login to Heroku

         Open your terminal and log in to your Heroku account:
         heroku login

         Create a Heroku App
         Create a new app on Heroku:
         heroku create your-app-name

      - Add MySQL Add-on

         Add the ClearDB MySQL add-on (or another MySQL add-on of your choice):
         heroku addons:create cleardb:ignite

         This will provision a MySQL database and provide a DATABASE_URL environment variable.

      - Set Environment Variables

         Configure the environment variables that python-decouple will use. You can dothis through the Heroku CLI or the Heroku Dashboard. Here's how to set environment variables using the Heroku CLI:
         
         heroku config:set DJANGO_SECRET_KEY='your-secret-key'
         heroku config:set DJANGO_DEBUG=False
         heroku config:set ALLOWED_HOSTS='yourdomain.com'
         heroku config:set DATABASE_URL='your-cleardb-database-url'

      - Push Code to Heroku
         Initialize a Git repository if you haven’t already:

         git init
         git add .
         git commit -m "Initial commit"

         Push to Heroku:
         git push heroku master

         Run Migrations:
         heroku run python manage.py migrate

         Create a Superuser (Optional):
         heroku run python manage.py createsuperuser

         Collect static files for production use:
         heroku run python manage.py collectstatic --noinput

   3. *Verify Deployment*

         Once the deployment is complete, open your app in the browser:

         heroku open
         Check that your app is running correctly and verify that all features work as expected.




