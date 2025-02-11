# The Village Tap

The village tap is a news site designed for the community of a small, fictional Irish village. 

The site is designed to provide the imagined community with up-to-date news about village happenings, including traffic updates, wedding announcements, and more. It also serves as a platform for engaging discussions on the site's articles, as well as an open forum for community members to share thoughts and seek opinions on various topics.

[Live link to the site]()

![The Village Tap website responsiveness](docs/images/responsive.gif)


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
   
* [Blueprint](#blueprint)
     * [Wireframe Models](#wireframe-models)
     * [Database Model](#database-model)

* [UI and Layout](#ui-and-layout)
     * [Implemented Features](#implemented-features)
     * [Features to be implemented](#features-to-be-implemented)
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

The platform offers an intuitive experience, allowing users to easily read articles, participate in forum discussions, and leave comments. Administrators have the ability to manage and create articles, moderate user content, and maintain a safe community environment through the admin dashboard. The interface is fully responsive, ensuring smooth navigation across all devices.


### UX Design
The UX design focuses on providing a seamless and intuitive experience for all users. The layout is clean and easy to navigate, ensuring that users can quickly find and engage with content. Key elements, such as articles and forum discussions, are prominently displayed to enhance accessibility. The design prioritizes responsiveness, adapting effortlessly across devices to ensure a smooth experience on both desktop and mobile. Clear calls to action and thoughtful interaction design guide users through the site, creating a positive and engaging environment.

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
Guided by the milestones, goals, and user stories, the following features and functionalities were planned:

* Responsive Design:
   
   Ensures full functionality and proper resizing across all devices, starting from 360px width upwards.

* Mobile/Tablet Optimization:
   
   Utilizes a toggle-menu and hidden elements (e.g., home page image) to improve site viewing on mobile and tablet devices.

* Public Section (Non-Restricted Access):
  
  A dedicated section of the site for general information, accessible by all users:
   * Village News & Announcements
   * Event Listings
   * General Articles

* User Interaction Section (Restricted Access):
  
  A space for community members to interact, including CRUD (Create, Read, Update, Delete) functionalities for user accounts and participation:
   * User Registration/Sign In/Out
   * Create and Edit Forum Posts
   * Comment on Articles
   * Participate in Discussions

* Admin Section (Restricted Access):
  
  A secure admin backend to manage site content and user interactions, including CRUD functionalities for site administrators:
   * Manage Articles (Create, Edit, Delete)
   * Moderate Comments and User Contributions
   * View and Manage User Accounts
   * Ensure Site Safety and Content Quality

## Structure

With the Strategy and Scope clearly defined, the next step was to structure the site in a way that ensures intuitive navigation and functionality. To achieve this, clear acceptance criteria were established for each feature, ensuring that every componennt aligned with user needs and project goals. This structured approach guided developement and provided a framework for maintaning usability, accessibility and responsiveness across all devices.

The website is organised into three main sections: 

* Public Section (Accessible to all users):
   * Display all available articles eith all their content.
   * Provides Articles are categorised for easy browsing, which allows users to quickly find the content they are looking for.
   * Designed to be engaging and useful even for visitors who are not registered.

* User Interaction Section (Rgistered users only)
   * Enables community engagement through participation in forum discussions.
   * Allows users to create, edit, and delete forum posts and comments, providing an interactive space for community conversations.
   * A simple and accessible authentication system allows users to register. log in and log out.

* Admin Section (Administrators only)
   * A secure backend dashboard provides tools to manage site content and user interactions.
   * Includes CRUD functionalities for news articles and forum posts.
   * Moderation tools ensure content quality and a safe discussion environment.
   * A front-end NavLink to the "Create New Article" page is only visible to logged-in admins.


## Blueprint

Before development began, wireframes were created to outline the site's layout and user flow. These provided a visual guide for how key features, such as navigation, forum discussions, and news articles, would be structured and presented. In addition, a database schema was designed to define how data would be organized and interconnected within the project. Taking the time to plan both the interface and data flow ensured a more efficient and structured approach to development.

### Wireframe Models

#### Main Site Pages

1. Home
  
 * Article detail pages 

![Home page](docs/images/wireframe-index_page.png)

![Article Detail Page](docs/images/wireframe-article_detail.png)

2. The Snug Forum
 
 * Thread detail pages

![The snug forum](docs/images/wireframe-the_snug.png)

![Thread detail page](docs/images/wireframe-thread_detail.png)


#### Authorisation Pages

* Register
* Sign in 
* Sign out

![Register](docs/images/register.png)

![Sign in](docs/images/login.png)

![Sign out](docs/images/logout.png)


#### Create New Article Page (For Administrators only)

![Create New Article Page](docs/images/create_new_article.png)



### Database Model

The database for this project is built around Django’s built-in User model, which handles authentication. Everything else - articles, forum threads, and comments - connects back to users in a one-to-many relationship. This basically means that one user can write multiple articles, start multiple forum threads, and leave multiple comments, but each article, thread, or comment belongs to just one user.

There’s also a connection between threads and articles, so discussions in the forum can be linked to news posts if needed. This is optional, threads do not have to be tied to an article at all.

The diagram below lays out how everything is connected in the database.


![ER Diagram](docs/images/diagram.jpeg)

## UI & Layout

With the wireframes and database structure sorted, the site was put together using Django, HTML, CSS, and JavaScript to bring all the planned features to life. Each page was built to match the original idea while making sure everything was responsive and easy to use. Below are screenshots showing how the final version of the site turned out.

### Implemented Features

The following features were developed based on the project’s goals and user needs. Each one was designed to enhance functionality and improve user experience, ensuring the site is both practical and engaging. Details for each feature are provided below.

#### Navbar and Toggler

* A fixed navbar appears on all pages, making it easy to move around the site without having to scroll back up.
* Includes links to Home, The Snug (Forum), and Register/Login, giving users quick access to key areas.

![navbar](docs/images/navbar.png)

* A Categories dropdown lets users filter articles by topic, making it simple to find specific news sections.

![navbar categories](docs/images/categories_nav.png)

* The navbar automatically switches to a collapsible toggler menu on smaller screens to keep things looking neat.

![Nav toggler](docs/images/toggle_nav.png)

* If an admin is logged in, a "Create New Article" link appears, allowing them to quickly access the article creation page. Regular users don't see this option.

![Navbar admin](docs/images/navbar_admin.png)


#### Footer

* Stays at the bottom of every page, making sure users always have quick access.
* Links to social media (Facebook, Twitter, Instagram, YouTube) so users can stay updated.
* Uses Font Awesome icons for a clean look instead of plain text links.
* Dark background for contrast, making it easy to read and stand out.
* Fully responsive, so it looks good on both big screens and mobiles.

![Footer](docs/images/footer_all_pages.png)

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
I used ChatGPT to create the fictional articles on the website.

### Media

### Acknowledgments

I would like to thank my Code Institute mentor, Graeme Taylor, for his continuous guidance and support throughout this project.






