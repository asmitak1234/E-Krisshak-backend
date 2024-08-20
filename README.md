# E-Krisshak-backend
<!-- explaining setup,functionalities, and deployment steps. -->
<!-- ## for heading, # for main heading,following for links and lists ,[CONTRIBUTING.md](CONTRIBUTING.md) file for locating to file.-->


## Description

Hello Everyone, I am ASMITA KUMARI ,a young learner and i am here with my project called "E-Krisshak" , A farmer availability management system that helps to find a farmer for your field with their proper and detailed Personal, Professional and Contact information that helps you to choose them according to your requirements. I am making this project with the intension of helping the land-owners that can't find farmer for their field and many farmers that are seeking for work ,especially in INDIA.

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
   cd frontend
   

2. *Install Frontend Dependencies*

   bash:
   npm install  # or yarn install
   

3. *Start the Development Server*

   bash:
   npm start  # or yarn start
   

   The frontend will typically run on http://localhost:3000.

## Connection 

- *Frontend-Backend*: Frontend and Backend is connected by Axios library.
- *Backend-Database*: Backend and Database is connected by updating Database information in settings.py after creating database.
 
For Security reasons you can add .env file to protect your sensitive data from settings.py and including it in [.gitignore](.gitignore) file.

## Functionalities

- *User Authentication*: Users can register and log in to their profiles.
- *Navigation*: Users can navigate to different web pages(Home , List , Manage) through Side Navigation Bar.
- *CRUD Operations*: Perform create, read, update, and delete operations on the main resources.
- *Responsive Design*: The frontend is designed to be responsive and works on various devices.
- *API Integration*: The frontend communicates with the backend via a RESTful API.

## Deployment

1. *Build the Frontend for Production*

   bash:
   npm run build  # or yarn build
   

   This will create a build directory with static files for production.

2. *Serve Static Files in Django*

   - Update ekrisshakbackend/settings.py to serve static files:

     python:
     STATICFILES_DIRS = [os.path.join(BASE_DIR, 'ekrisshakfrontend/build')]
     

   - Ensure django.contrib.staticfiles is in your INSTALLED_APPS.

3. *Configure Gunicorn and Nginx*

   - *Install Gunicorn*:

     bash:
     pip install gunicorn
     

   - *Run Gunicorn*:

     bash:
     gunicorn --bind 0.0.0.0:8000 my_project.wsgi
     

   - *Set Up Nginx*:

     Configure Nginx to serve the Django application and the React build directory. Example Nginx configuration:

     nginx:
     server {
         listen 80;
         server_name your_domain_or_ip;

         location / {
             root /path/to/your/repo/frontend/build;
             try_files $uri /index.html;
         }

         location /api/ {
             proxy_pass http://127.0.0.1:8000;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     

4. *Set Up a Database Production Configuration*

   Update your DATABASES settings in `ekrisshakbackend

5. *Secure Your Application*

   - Set DEBUG = False in ekrisshakbackend/settings.py.
   - Set up proper security settings, including ALLOWED_HOSTS, SECRET_KEY, and HTTPS.

