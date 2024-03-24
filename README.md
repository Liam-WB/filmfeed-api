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
    * Developer User Stories
    * User Stories
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

## Database structure

### Features

The backend API (Built with Django Rest Framework) used 2 different buiilds depending on development stages. The first was the development build which was connected to a local SQL database for testing purposes. The project implemented generic views to allow developers to use create update views to create, update and delete data via the view using GET and POST requests. On the other hand, the production build (predominantly used only for storing data rather than creating via the live project for simplicity), is connected to a PostgresQL database via [Railway](https://railway.app/project/349253d3-daa3-45c1-90ec-dfc1af58bb4e), which can be accessed to view all the data and its variables in easily accessible rows and columns.

#### Homepage

When entering the API, you'll be directed to the root route homepage, and greeted with the API's welcome message to confirm you've successfully entered the site.

![Welcome message](md_images/Screenshot%202024-03-24%20205224.png)

#### Profile Data

The profile model view will display a list of profiles, each containing their respective data fields. Each data field will return data (or null) depending on the data created via form submission, admin panel, superuser creation. The profiles list view can be accessed via the url/address bar. And individual profiles/ profile information can be displayed by adding "/profile_id" to the end of the url. As mentioned above, the create functionality is not included via the live backend project as the functionality is passed on to the frontend. The below message is shown upon errors finding profile data. The views are developed with generic views, and filter fields are developed with Django Filter Backend.

![Data not found](md_images/Screenshot%202024-03-24%20211429.png)

![Profiles page](md_images/Screenshot%202024-03-24%20221422.png)

##### Profile model fields: ///

* owner
* created_at
* updated_at
* name
* bio
* image

##### Profile model serializer fields:

* is_owner
* following_id
* user_type
* posts_count
* followers_count
* following_count

##### Ordering / filtering methods, parameters:

* owner__following__followed__profile
* owner__followed__owner__profile
* posts_count
* followers_count
* following_count
* owner__following__created_at
* owner__followed__created_at

In the development build there is a search function for returning specific profiles and their data, as well as a filter box to filter profiles depending on the given parameters.

* Filter option and results are returned for user's followers' profiles.
* Filter option and results are returned for users' profiles that the user is following.

In the development build the edit/update form is displayed for logged in users for changing profile data. A delete button is also displayed to logged in profile owners. The update form is pre populated with current profile information, and upon profile deletion all other profile data cascades to delete all unneeded and related data.

#### Post Data

The post model view will display a list of profiles, each containing their respective data fields. Each data field will return data (or null) depending on the data created via form submission, admin panel, superuser creation. The posts list view can be accessed via the url/address bar. And individual posts/ post information can be displayed by adding "/post_id" to the end of the url. As mentioned above, the create functionality is not included via the live backend project as the functionality is passed on to the frontend. The views are developed with generic views, and filter fields are developed with Django Filter Backend.

![Post list](md_images/Screenshot%202024-03-24%20211355.png)

![Welcome message](md_images/Screenshot%202024-03-24%20211457.png)

##### Post model fields:

* owner
* created_at
* updated_at
* title
* content
* image
* movie

##### Post model serializer fields:

* is_owner
* profile_id
* profile_image
* like_id
* likes_count
* comments_count

##### Ordering / filtering methods, parameters:

* owner__followed__owner__profile
* likes__owner__profile
* owner__profile
* owner__username
* title
* movie
* likes_count
* comments_count
* likes__created_at

In the development build there is a search function for returning specific posts and their data, as well as a filter box to filter posts depending on the given parameters.

* Posts who's user is followed by the logged in user will be displayed as the "feed" page in the frontend.
* Posts which the user has liked by the user will be displayed as the "liked" page in the frontend.
* All posts posted by the user or by a specific user will be displayed in the profile page.

As mentioned above, in the development build the create form is displayed for logged in users for creating posts. A delete button and update form is also displayed to logged in post owners on their respective post pages. The update form is pre populated with current post information, and upon post deletion all other post data cascades to delete all unneeded and related data.

#### Movie Data

The movie model view will display all logged movies, each containing their respective data fields. Each data field will return data depending on the search query and ultimately, logged movie. The movies list view can be accessed via the url/address bar. And individual movies/ movie information can be displayed by adding "/movie_id" to the end of the url. 

In this case, the movies model here does not currently store the site's logged movies as they are stored and attached to the post model for linked movie data, and although the movies can be fetched in the development build's added search bar for movies, for performance purposes it was more efficient to fetch the movie data via the frontend, seeing as the data is read only.

![Movies list](md_images/Screenshot%202024-03-24%20224019.png)

##### Movie model fields:

* title
* movie_data

##### Post model serializer fields:

* id

##### Ordering / filtering methods, parameters:

* title

As mentioned above, there is a filter option to allow users to change their search queries depending on movie title. They are also able to log movies to the api by searching a movie title which in turn requests a movie with the closest name to the search query, via the omdb api which will then return the movie's information and categorise it in it's respective fields. The data returned is parsed as JSON, making the data easily readable.

#### Likes Data

Within the likes model list view in the DRF API, users can view a full list of all logged post likes in the app.

![Likes list](md_images/Screenshot%202024-03-24%20230148.png)

##### Likes model fields:

* owner
* post
* created_at

If the user is logged in, the create form is displayed to create a new like. The post they want to like can be selected on the form. Users are unable to like the same post twice, as they'll receive an error message reading that they can't like the same post, and duplicate likes can't be created. If a user attempts to like a post they created, the API will return an error message saying that they can't like their own post and the like was not created. Just like above, logged in users are given functionality to delete their own likes.

#### Comments Data

Within the comments model list view in the DRF API, users can view a full list of all logged post comments in the app.

![Comments list](md_images/Screenshot%202024-03-24%20230641.png)

##### Comments model fields:

* owner
* post
* created_at
* updated_at
* content

##### Comments serializer fields:

* is_owner
* profile_id
* profile_image

##### Ordering / filtering methods, parameters:

* post

In the development build, a filter box was implemented to filter the comments by the post they are linked to. If the user is logged in, a create form is displayed. Just like the likes create form, the user is given the option on what post to create their comment. On the comment post page the user is given edit and delete functionality if they own the comment. Just as before, a pre-populated form is returned for the edit functionality.

#### Followers Data

Within the followers model list view, users can view a full list of all logged profile followers in the app.

![Followers list](md_images/Screenshot%202024-03-24%20232212.png)

##### Followers model fields:

* owner
* followed
* created_at

##### Followers serializer fields:

* followed_name

Logged in users will receive a form for creating a new follower post. The user is able to select the profile for the follow submission. If a user tries to follow the same profile twice, they'll receive an error message reading that they're already following the selected profile, and the duplicate follow post is unable to be created. Once logged in, if the user views their own follow, additional Delete functionality becomes visible.

## Database skeleton

### Database design

#### ERD (Entity Relationship Diagram)

The following ERD was concepted using the above data, models and fields. The relationships between all these models are also shown in the diagram:

![ERD](md_images/Initial%20regular%20user%20ERD.png)

* The data model logic was developed using this ERD as a plan.

As shown in the ERD all data types are directly connected to the users, and therefore if a user is deleted from the database, all related information is also removed from the database, as intended. Initially the movies model was named the watch history and would function slightly differently: It was planned to contain the logic for a component that would later be added within the profile page, as a secondary container for profile information, however it was later decided that a movie model, and movie data that connects to a post would be more beneficial as the movie implementation would be in the forefront of the website and more visible. With more time, a watchg history model would have been created, as shown in the project future consideration user stories category.

## Testing

Please click this [link](#) to view the filmfeed DRF API TEST.md file.