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

This projected was planned, managed and developed with agile methodologies in mind to provide the developer with an efficient and effective development process. This was done by delivering small features to the project step by step, allowing for easier project management, organisation and allowing each function to be given the detail and attention that is required. I started by creating a kanban board, developed in github projects and used this as the main project management, and organisation to help visualise the project priorities, limit in progress, and maximise the work flow/efficiency to make the frontend development process simpler.

Filmfeed DRF API kanban board [link](https://github.com/users/Liam-WB/projects/8/views/1)