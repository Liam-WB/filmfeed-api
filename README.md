# Filmfeed DRF API

"Filmfeed" is a movie enthuasiast's take on a social media website, made for all types of users who are interested in sharing their experience and journey. Whether you're a casual watcher or a critic, filmfeed is tailor-made to welcome all, new-face or old to create connections and meet like-minded watchers!

This README.md is for the project backend. For more information on the project frontend, please visit [this link](https://github.com/Liam-WB/filmfeed).

--

The filmfeed DRF API provides create, view, edit, delete functionality for user related data management, user related authentication levels to ensure secure access to authentication-locked pages for securing sensitive data, and a safe, secure database for storing the user's content. The database provides the project with the data required for the functionality for the usual social media features in profiles, posts, likes, followers, comments, as well as movie related implementation. The database also allows users to request and receive search querie's based on a data type's paramaters and relationships. E.g. if the user wants search results for a post's title name or the most popular profiles, the database will be able to return the requested items. All data models are equipped with custom serializers, to validate items being stored within the database and making sure that the logic for the data fits the data category's criteria. Appropriate error messages are intended to be returned upon receiving data or search queries that do not match the expected paramaters.

Live API [link](https://filmfeed-api-d8205608db2c.herokuapp.com/).

API Project (Heroku) [link](https://dashboard.heroku.com/apps/filmfeed-api).

## Directory of contents

* Database strategy
    * Agile Methodology
    * Epics
    * Target Audience
* Database structure
    * Features
* Database skeleton
    * Database Design
* Technologies
* Testing
* Deployment
* Credits
---

### Agile project planning

This projected was planned, managed and developed with agile methodologies in mind to provide the developer with an efficient and effective development process. This was done by delivering small features to the project step by step, allowing for easier project management, organisation and allowing each function to be given the detail and attention that is required. I started by creating a kanban board, developed in github projects and used this as the main project management, and organisation to help visualise the project priorities, limit in progress, and maximise the work flow/efficiency to make the frontend development process simpler. The user stories were colour coded with green, yellow, purple, red to categorise functions depending on priority and work progress.

Filmfeed DRF API kanban board [link](https://github.com/users/Liam-WB/projects/8/views/1)

![Kanban](md_images/Screenshot%202024-03-24%20200746.png)

### Epics

* Set up a workspace

User stories were categorised into the 2 following milestones:

* Frontend resources
* Backend/API resources

### Developer User Stories

* As a developer I can create the navbar and footer with their respective features so that I can navigate different pages on the website and locate any import information/links
* As a developer I can create a log in, log out, sign up form so that users can create, switch, or leave their accounts on the website
* As a developer I can create a profile page so that users can access and edit their profile information/content
* As a developer I can create a post form page so that users can create, edit and update their own posts
* As a developer I can create a post detail page so that view a specifc post and its details
* As a developer I can create the homepage so that users can interact with the available functions and content on the homepage
* As a developer I can create the movies/TV shows app/feature so that they can be stored in my drf api and movies/TV shows can be associated with other app features e.g. profiles, posts
* As a developer I can create the search feature so that specific object id's can be located via object name, and stored in my drf api
* As a developer I can create the filter feature so that objects within the drf api can be located and categorised depending on their specific attributes
* As a developer I can create the comment like feature so that comment likes can be stored in my drf api
* As a developer I can create the comment reply feature so that comment replies can be stored in my drf api
* As a developer I can sign in, out and up so that I can switch to a different desired account
* As a developer I can create simple account and (admin) superuser accounts, as well as permission lock simple accounts so that developers can access permission locked features and users willl be able to view the site as intended
* As a developer I can create the comments app so that comments can be stored in my drf api
* As a developer I can create the followers app so that followers can be stored in my drf api
* As a developer I can create the likes app so that likes can be stored in my drf api
* As a developer I can create the posts app so that my posts can be stored in my drf api
* As a developer I can create the profiles app so that profiles can be stored in my drf api
* As a developer I can create a frontend folder containing a react project so that I can develop a frontend application to execute backend logic
* As a developer I can set up a django project so that I can create the apps/code components
* As a developer I can create a movie page so that users can find movies and their related information
* As a developer I can create data validation alerts so that users know if their submitted data is valid

#### User stories

* As a user I can see a list of recommended/relevant profiles/posts and movies so that my feed contains relevant content/movies/information
* As a user I can view a paginated list of posts (ordered from most recent) so that I can view relevant content on my feed (ordered from most recent)
* As a user I can access a post content form so that I can edit, update or create a post
* As a user I can delete my account so that my information is removed from the database
* As a user I can access respective profile create/signin,out/update forms so that I can create, leave, edit and update my profile
* As a user I can search and filter content so that I can recieve categorised/specific results based on my search
* As a user I can log in and out or create an account as intended so that I can access logged in features and exit my profile
* As a user I can view posts so that I can view site content/post details
* As a user I can view others' comments so that I can see conversations associated with the related post
* As a logged in user I can create, edit or update and delete posts so that I can change my profile's released content and post details
* As a logged in user I can like a post so that the user knows their post has been viewed and I liked the content
* As a logged in user I can comment on a post so that users can interact with the post and conversate about the content
* As a logged in user I can reply to a comment so that the comment turns into a discussion/conversation
* As a logged in user I can like a comment so that I can interact with a user and indicate I enjoyed their comment
* As a logged in user I can update my profile so that others can view my profile information
* As a logged in user I can link movies to my post so that I can show others what movie I am watching