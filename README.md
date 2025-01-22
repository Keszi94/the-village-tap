# The Village Tap

The village tap is a news site designed for the community of a small, fictional Irish village. 

The site has been designed to allow the imagined community members to get up-to-date news about happenings in the village (traffic updates, wedding announcements, etc.) and to open up discussions about the site's articles, or just to create an open forum to talk about whatever they'd like their neighbours opinions on. 

[Live link to the site]()

![The Village Tap website on different devices]()


## CONTENTS

* [User Experience](#user-experience)
     * [UX Design](#ux-design)

 * [Planning](#planning)
     * [Milestones and User Stories](#milestones-and-user-stories)
         * [Milestone 1 - Initial Setup](#milestone-1---initial-setup)
         * [Milestone 2 - Main Site Pages](#milestone-2---main-site-pages)
         * [Milestone 3 - Forum Access](#milestone-3---forum-access)
         * [Milestone 4 - CRUD Functionality](#milestone-4---crud-functionality)
         * [Milestone 5 - Additional](#milestone-5---additional)
   
* [Scope](#scope)
   
* [Structure](#structure)
   
* [Back-End Design](#back-end-design)
     * [Database Schema](#database-schema)
     * [Models](#models)
     * [Implemented Features](#implemented-features)
     * [Features To Be Implimented](#features-to-be-implemented)

* [Front-End Design](#front-end-design)
     * [Wireframe Models](#wireframe-models)
     * [Design and Typography](#design-and-typography)

* [Tecnologies and Resources Used](#technologies-and-resources-used)

* [Testing](#testing)

* [Deployment & Local Development](#deployment--local-development)
     * [Heroku Deployment](#heroku-deployment)
     * [How to Fork](#how-to-fork)
     * [How to Clone](#how-to-clone)

* [Credits](#credits)
     * [Code Used](#code-used)
     * [Content](#content)
     * [Media](#media)
     * [Acknowledgments](#acknowledgments)


## User Experience

This platform provides an intuitive experience for site users to read articles, participate in forum discussions, and comment freely. Administrators can manage and create articles, moderate user content, and ensure safe community environment through the admin dashboard. The interface is responsive and designed for seamless navigation across devices.


### UX Design


## Planning

### Milestones and User Stories

#### Milestone 1 - Initial Setup
- 1: Install and configure Django along with necessary libraries in the IDE to start development
- 2: Set up project and apps with the required structure and configurations
- 3: Deploy the project to Heroku with for early testing
- 4: Create an instance of a cloud-based PostgreSQL database and connect it to the project
- 5: Create a random secret_key and add it to the env.py file
- 6: Create and Setup The Forum App

#### Milestone 2 - Main Site Pages
- 1: Site Admin User Story: Add and manage news stories (back-end)
- 2: Site Admin User Story: Assign Categories to Articles
- 3: Site User User Story: View a news article
- 4: Site User User Story: View the Homepage
- 5: Site User User Story: News Categories

#### Milestone 3 - Forum Access
- 1: Site User User Story: Account Registration
- 2: Site User User Story: View "The Snug" forum page

#### Milestone 4 - CRUD Functionality
- 1: Site Admin User Story: Make the text area for news editing intuitive
- 2: Site Admin User Story: Thread Creation From Front-end
- 3: Site Admin User Story: Creating new articles from the main page
- 4: Site User User Story: Thread Creation
- 5: Site User User Story: Threads edit and deletion
- 6: Site User User Story: Commenting in "The Snug" Forum
- 7: Site User User Story: Edit and Delete Comments

#### Milestone 5 - Additional
- 1: Dev: Automatically Created Forum Threads for New Articles
- 2: Site Admin User Story: Review & Handle News Suggestions
- 3: Site Admin User Story: Add New Category If Needed
- 4: Site User User Story: News Suggestions


## Scope


## Structure


## Back-End Design

### Database Schema

### Models

### Implemented Features

#### Navbar

#### Footer

#### Home Page

#### Forum Page
##### Thread Creation
##### Thread list
* Thread Editing
* Thread Deletion
#### Commenting
* Comment Editing
* Comment Deletion

#### Sign Up/In/Out

#### Admin Panel


### Features To Be Implimented


## Front-End Design

### Wireframe Models

### Design and Typography


## Tecnologies and Resources Used

### Tecnologies

In order to code and design the website, the following technologies were utilised:

* Python Modules:
  * asgiref==3.8.1
  * dj-database-url==0.5.0
  * Django==4.2.17
  * django-allauth==0.57.2
  * django-summernote==0.8.20.0
  * gunicorn==20.1.0
  * oauthlib==3.2.2
  * psycopg2==2.9.10
  * PyJWT==2.10.1
  * python3-openid==3.2.0
  * requests-oauthlib==2.0.0  
  * sqlparse==0.5.3
  * whitenoise==5.3.0

* Django


* Heroku


* Bootstrap


* CSS


* JavaScript


* CI Database Maker



## Testing


## Deployment & Local Development

### Heroku Deployment

This site is deployed to and currently hosted on the Heroku platform. The steps for deploying to Heroku with a custom PostgreSQL database setup are as follows:

1. PostgreSQL Database Setup
 * Navigate to [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/).
 * Enter your student email address in the input field provided.
 * Click Submit.
 * Wait while the database is created.
 * Once the database is successfully created, check your student email inbox for further details.

2. Django Project Settings

* In the project workspace, navigate to/create a file named Procfile (remember the capital 'P'). Add the following code (replace <myapp> with your actual app name) and save the file:
  ```makefile
  web: gunicorn <myapp>.wsgi
   ```
* Now, create a file named env.py and add the following code, replacing <myurl> with your database URL and <mykey> with a secret key string. Save the file:
  ```python
  import os

  os.environ["DATABASE_URL"] = <myurl>
  os.environ["SECRET_KEY"] = <mykey>
  ```
* Open settings.py and add the following imports near the top of the file:
  ```python
  import os
  import dj_database_url
  if os.path.isfile('env.py'):
    import env
  ```
* Replace the SECRET_KEY and DATABASES variables with the following:
  ```python
  SECRET_KEY = os.environ.get('SECRET_KEY')

  DATABASES = {
      'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
  ```
* Save the file, then run ```python manage.py migrate``` in the terminal to apply any database migrations.

3. Push Changes to Repository
 * Commit and push these changes to the repository to update your project.

4.  Heroku Setup
* Navigate to Heroku and log in or create an account.
* Click "New" in the top right and select "Create New App."
* Enter a unique app name, choose a region, then click "Create app."
* Go to the "Settings" tab and click "Reveal Config Vars." Add the following:
     * ```DATABASE_URL```: Your database URL from the previous setup.
     * ```SECRET_KEY```: Your secret key.
     * ```PORT```: 8000 (default port for Heroku apps).
* Go to the "Deploy" tab, select "GitHub" under "Deployment method," and connect your repository.
* Scroll down and click "Deploy Branch" to complete the deployment process.


### How to Fork

1. Log in to your GitHub account.
2. Navigate to the ['The Village Tap' GitHub repository](https://github.com/Keszi94/the-village-tap).
3. In the top right corner of the page, click the "Fork" button.
4. Select your GitHub account or organization where you want to fork the repository.
5. You now have a copy of the repository in your own account to make changes.

### How to Clone
1. Log in to your GitHub account.
2. Navigate to the ['The Village Tap' GitHub repository](https://github.com/Keszi94/the-village-tap).
3. Click on the "Code" button and ensure "HTTPS" is selected.
4. Copy the repository URL.
5. Open your terminal/command line, navigate to the folder where you want to clone the project, and run:
```python
git clone <repository-url>
```

## Credits

### Code Used

### Content

### Media

### Acknowledgments






