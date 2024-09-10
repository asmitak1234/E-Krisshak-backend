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

   git clone https://github.com/asmitak1234/E-Krisshak-backend.git
   cd E-Krisshak-backend
   

2. *Create and Activate a Virtual Environment*

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install Backend Dependencies*

   pip install -r requirements.txt
   

4. *Configure the Database*

   - Create a MySQL database and user. Update the database settings in [ekrisshakbackend/settings.py](ekrisshakbackend/settings.py):

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

   python manage.py migrate
   

6. *Create a Superuser*

   python manage.py createsuperuser
   

7. *Run the Development Server*

   python manage.py runserver

    The Django Backend development server will typically run on http://127.0.0.1:8000/.
   
Other Requirements are in the file [requirements.txt](requirements.txt)

### Frontend Setup

1. *Navigate to the Frontend Directory*

   cd ekrisshakfrontend
   

2. *Install Frontend Dependencies*

   npm install  # or yarn install
   

3. *Start the Development Server*

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

   ### Overview
      This project involves deploying a Django backend to Vercel, while using AlwaysData for the database. Follow these steps to deploy the application successfully.

   ### Prerequisites

   Before deploying the backend, ensure you have the following:
   
   - Django Project: Ensure your Django project is set up and working locally.
   - Vercel Account: Sign up for a Vercel account if you don't have one.
   - AlwaysData Account: Sign up for an AlwaysData account if you don't have one.
   - Git: Ensure Git is installed and configured on your local machine.

   ### Steps to Deploy

   1. *Setup AlwaysData for the Database*

      Create a Database:

      Log in to your AlwaysData account.
      Go to the “Databases” section and create a new database.
      Note the database name, user, password, and host information.

      Configure Django Settings:

      In your Django project, update the DATABASES settings in settings.py to use the AlwaysData database credentials. Example:

      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'your_db_host',
            'PORT': '3306',
         }
      }

      Install gunicorn and whitenoise and include whitenoise's middleware.
      
      Apply Migrations:

      Run Django migrations to set up the database schema:
      python manage.py migrate

   2. *Deploy Django Backend to Vercel*

      Prepare the Django Project:

      Make sure you have a vercel.json file in the root of your project to configure the Vercel deployment. Example:

      {
         "builds":[
            {
                  "src":"your_project_name/wsgi.py",
                  "use":"@vercel/python",
                  "config":{"maxLambdaSize":"15mb","runtime":"python3.9"}
            }
         ],
         "routes":[
            {
                  "src":"/(.*)",
                  "dest":"your_project_name/wsgi.py"
            }
         ]
      }

      Ensure you have gunicorn in your requirements.txt or Pipfile:
      
      Login to Vercel:

      Login to vercel and click on new project,
      Connect it to github and,
      After pushing all the changes to github ,Select the repository to be deployed
      

      Configure Environment Variables:

      Set environment variables for your Django project in Vercel for deployment and click 'Deploy' button.


   3. *Post-Deployment*

      Collect Static Files:

      Ensure static files are collected for your Django app:

      python manage.py collectstatic --noinput
      
      Check the Deployment:

      Visit the Vercel deployment URL to ensure everything is working correctly.
      Monitor Logs:

      Use Vercel’s dashboard to monitor logs and troubleshoot any issues that arise.

