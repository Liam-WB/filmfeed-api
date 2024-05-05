# Filmfeed DRF API | Tests

Return to [README.md](/README.md)

--

Comprehensive testing has been done to ensure that the project's functions and features work flawlessly, and without issue.

## Directory of Contents

* Responsiveness Tests
* Code Validation
* Bugs
    * Resolved Bugs
    * Unresolved Bugs
* Manual/features Tests

### Responsiveness tests

The responsiveness tests were mainly composed of device, viewport, browser and compatability tests. The deployed Filmfeed DRF API has underwent rigorous and frequent testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Developer Tools were utilized to simulate various screen sizes, enabling thorough examination of how the website behaves across different devices. The API was also tested on different web browsers, in tandem with it's frontend half to ensure that there were no errors or issues being caused between them. Due to the nature of the API being mainly backend, these tests were more focused on performance and functionality.

### Code validation

#### PEP8
The filmfeed API has been developed with the pylint extension to provide formatting, linting and internal PEP8 validation tests. No problems or warnings were found.

#### Automated Testing
7 automated tests were written for the posts and profiles models to test user story scenarios. No problems or warnings were found.

### Bugs

#### Resolved Bugs
* Bug where JSON data was not parsing properly into the movie model - Fixed by importing and using JSON Field.

#### Unresolved Bugs
* Django Rest Framework API admin panel not showing CSS although static files are connected in cloudinary. (This could likely be fixed by reconnecting/connecting new static files, however I did not get around to this.)

### Features tests

I carried out additional manual tests listed below:

Profiles

✓ Profile List can be ordered by posts_count in ascending order

✓ Profile List can be ordered by posts_count in descending order

✓ Profile List can be ordered by events_count in ascending order

✓ Profile List can be ordered by events_count in descending order

✓ Profile List can be ordered by followers_count in ascending order

✓ Profile List can be ordered by followers_count in descending order

✓ Profile List can be ordered by following_count in ascending order

✓ Profile List can be ordered by following_count in descending order

Posts

✓ Posts List can be ordered by comments_count in ascending order

✓ Posts List can be ordered by comments_count in descending order

✓ Posts List can be ordered by likes_count in ascending order

✓ Posts List can be ordered by likes_count in descending order

✓ Posts List can be searched by owner

✓ Posts List can be searched by content

✓ Posts List can be searched by tag

✓ Posts List can be searched by movie

Movies

✓ Movies can be searched by title

Comments

✓ Comment List can be filtered by post

Followers

✓ Followers List can be filtered by profile

Likes

✓ Likes List can be filtered by post