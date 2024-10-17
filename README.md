![Banner of the logo](/documentation/images/banner-of-website.webp)

# KUIDAORE
Hello Fellow Coders! 

This is KUIDAORE. A luxurious Japanese restaurant based in Malibu, California. It comprises of an online website with the ability to make reservations and provide user authentication.

The target audience are foodies who love sushi and high end restaurants.

Book your reservation now! [KUIDAORE](https://kuidaore-restaurant-3c1cdf981122.herokuapp.com/)

![KUIDAORE on different device widths](/documentation/images/kuidaore-on-different-screen-widths.webp)

Am I Responsive [Website](https://ui.dev/amiresponsive?url=https://8000-cjphawes-restaurantbook-1qwx7mg5tv9.ws.codeinstitute-ide.net/)

---

## Goals

#### My Goals
For this project I have aimed:
- For users to be able to make a reservation with as little navigation as possible
- For authenticated users to be able to provide feedback and review the website / restaurant.
- To provide a high-end design and functional booking system tailored to registered users.

#### External User Goals
For this project users want to be able to:
- Create a reservation with ease.
- Have the ability to change or delete their reservations whenever they want to.
- Leave a review for the website

---

## User Stories

| **As a** | **I can** | **So that** |
|----------|-----------|-------------|
| User | Reserve a time slot dictating the number of guests I would like attending | I can visit this restaurant with a certain number of friends |
| User | Navigate the website easily | I am able to find all the necessary requirements I need to create a reservation or leave a review |
| User | Send a cancellation for a reservation | My reservations are always up to date with the correct information |
| User | Get answers to any questions or queries I may have | I can make an informed decision whether or not I want to visit the restaurant |
| User | Register an account with the restaurant | My details are saved for ease of reservations the next time I intend to visit |
| User | Change the preferred language of the website | I am able to go through the website and understand it in my own language |
| User | View the menu before attending | I can decide what food I would like to eat |
| User | Review and send a feedback form to the restaurant | I can provide constructive criticism to improve their website or restaurant |
| User | Sign-up to the restaurants newsletter | I can receive information about promotions or any news/events |

### Project Board

GitHub Project Boards were used to manage the project. It helped me to prioritize the tasks and to keep track of my progress. 

![KUIDAORE Project Board](/documentation/images/project-board.webp)

This displays a mixture of completed, nearly completed and not started issues:
  - The In Progress column contains one issue that require one more action in it to be completed, which is a future feature with emailJS.
  - The Future Features column contains three issues, creating a review system for the restaurant, changing the language of the website for accessibility and creating a newsletter.

---

## Wireframes

[Take me to the Project Wireframes](/WIREFRAMES.md)

## ERD Model

[Take me to the Database Model](/ERDDIAGRAM.md)

## Features

### Home Page
![Landing page image](/documentation/images/landing-page-img-1.webp)

- The home page shows:
  - The user what the website is about immediately.
  - Easy and simple ways to navigate the website, displaying key buttons to where the user needs to go.

- The home page includes:
  - A navigation bar with the ability to authenticate as a user and log in / log out freely.
  - A timed carousel of images of the restaurants food
  - Three links which are crucial to the websites functionality, that redirect the user to the respective webpages.

![Landing page image](/documentation/images/landing-page-img-2.webp)

### About Page
![About page image](/documentation/images/about-page-img-1.webp)
- The About page includes:
  - Some text describing the background of the restaurant.
  - Image of the head Chef who made the restaurant famous.
  - Two additional links for further ease of navigation for the user.

### Menu Page
![Menu page image](/documentation/images/menu-page-img-1.webp)

- The Menu page includes:
  - A detailed menu for the customers to preview
  - A list of Wine & Sake options through the use of an additional modal element.

![Menu page image](/documentation/images/menu-page-img-2.webp)

### Reservations Page
![Reservation page image](/documentation/images/reservations-page-img-1.webp)

- The Reservations page includes:
  - Some small text for the user about cancellations
  - Depending on whether the user is logged in or not, will determine if they can view their already made reservations or not. Inside this area, they area able to also remove and update pre-existing reservations.
  - A modal form which allows users to create a reservation for the restaurant.

![Reservation page image](/documentation/images/reservations-page-img-2.webp)

### Viewing Reservations Page
![Viewing reservation page image](/documentation/images/view-reservations-img-1.webp)

- The reservation view includes:
  - All the reservations the user has created.
  - Options to modify or cancel the reservation completely

### Update Reservations Page
![Update reservation page image](/documentation/images/update-reservation-img-1.webp)

- The update reservation view includes:
  - The ability to change the reservation parameters set by the user when initially making the reservation.

### Delete Reservations Page
![Delete reservation page image](/documentation/images/delete-reservation-img-1.webp)

- The delete reservation view includes:
  - The ability to completely remove the reservation from the users log.

### FAQ Page
![FAQ page image](/documentation/images/faq-page-img-1.webp)

- The FAQ page includes:
  - A list of FAQ's asked by the customers for better ease of understanding for future customers
  - An additional link to the contact page in case they need to ask further questions.

### Contact Page
![Contact page image](/documentation/images/contact-page-img-1.webp)

- The Contact page includes:
  - Some key information about location and contact information.
  - Depending on whether the user is logged in or not will determine if the user is allowed to submit a review form for the restaurant.

![Contact page image](/documentation/images/contact-page-img-2.webp)

### Things to mention
- Added AllAuth however aren't using sites and social accounts models.
- Not using Summernote attachments.

### Future Features to Implement
- Options for logging in through Social accounts rather than just standard emails.
- An additional contact form for general queries.
- Better UI interaction with confirmations of reservations to emails as well as on screen prompts and confirmations of user actions.
- Restaurant Newsletter Form, which will incorporate sending out emails with JS.
- Add a button to automatically scroll back to the top of the page when users are viewing their reservations.
- Amalgamate the Contact page into the About page.

---

## Technologies Used

#### Languages
- [Python](https://docs.djangoproject.com/en/5.1/releases/4.2.15/)
- [JS](https://www.javascript.com/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

#### Frameworks
- [Django 4.2.15](https://docs.djangoproject.com/en/5.1/releases/4.2.15/)

#### Databases
- [Code Institutes Postgresql](https://www.postgresql.org/)

#### 3rd Party Imports
  - [Pip3](https://pypi.org/project/pip/)
  - [allauth](https://docs.allauth.org/en/latest/)
  - [summernote](https://pypi.org/project/django-summernote/)
  - [crispy forms with boostrap 5](https://django-crispy-forms.readthedocs.io/en/latest/)
  - [Gunicorn](https://gunicorn.org/)
  - [whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html)
  - [sqlparse](https://pypi.org/project/sqlparse/) 
  - [Psycopg2](https://pypi.org/project/psycopg2/)
  - [oauthlib](https://oauthlib.readthedocs.io/en/latest/)
  - [PyJWT](https://pyjwt.readthedocs.io/en/latest/)
  - [asgiref](https://pypi.org/project/asgiref/)
  - [dj-database-url](https://pypi.org/project/dj-database-url/)
  - [python3-openid](https://pypi.org/project/python3-openid/)
  - [requests-oauthlib](https://requests-oauthlib.readthedocs.io/en/latest/)

#### Other Tools
  - [Gitpod](https://www.gitpod.io/) was used as the main IDE and tool to write and edit code.
  - [Git](https://git-scm.com/) was used for the version control of the program.
  - [Github](https://github.com/) was used to upload and host my code for collaboration purposes.
  - [Heroku](https://dashboard.heroku.com/apps) was used for the deployment of the website.
  - [Lucidchart](https://www.lucidchart.com/pages/) was used for the creation of my ERD model. 
  - [W3C Validator](https://validator.w3.org/) was used to validate HTML5 code for the website.
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) was used to validate CSS code for the website.
  - [JShint](https://jshint.com/) was used to validate JS code for the website.
  - [Code Institute Python Linter](https://pep8ci.herokuapp.com/#) was used to validate Python code for the website.

---

## Testing

Please refer to the [TESTING.md](/TESTING.md) for all test-related documentation.

### Solved Bugs
- **Issue 1**: When submitting a review, the user would not be redirected back to the correct page.
  - _Solution_: I found it was to do with my function for submitting a review, I was not using `redirect()` but `render()` so the user staying on the same page.
- **Issue 2**: When showing a display message it would not disappear but would rely on a user to close it, this is not what I wanted.
  - _Solution_: I created a JS file solely for the function of alerts which made the messages fade away after 3 seconds.
  
  ```
  window.onload = function() {
    let alerts = document.querySelectorAll('.alert');

    if (alerts) {
        alerts.forEach(alert => {
            setTimeout(function() {
                alert.classList.add("fade");

                setTimeout(function() {
                    alert.remove();
                }, 300);
            }, 3000)
        });
      }
    };
  ```

- **Issue 3**: When trying to display a message, the correct message would not display. e.g. a successful log in message after confirming a reservation.
  - _Solution_: I originally had the messages for loop in the html template for each page. I instead moved this to the base.html template, which also further minified my code.

### Unsolved Bugs
- I was unable to Style the AllAuth html templates for Sign-up, Sign-in & Sign-out forms.
- Couldn't disable dates in the calendar from before current date for user to not select, when making or updating their reservations.
- When changing to a different screen width, the carousel images would not shrink proportionally.
- In the update_reservation.html, the if statement was showing an error in the code but still worked. 

```
<option value="17:00" {% if reservation.reservation_time|date:'H:i' == "17:00" %}selected{% endif %}>17:00</option>

```

### Mistakes 
There were eight mistakes while committing to Github.
- **022d1c5** - "feat:remove template views & add func for update rbookings" _Supposed to be_: "feat:remove template views & add func for update bookings"
- **e7a764c** - "add migrations" _Supposed to be_: "maint:add migrations"
- **6372021** - "add js for form function" _Supposed to be_: "feat:add js for form function"
- **aaa44d1** - "adjust bs5 classes added to html" _Supposed to be_: "feat:adjust bs5 classes added to html"
- **0c74670** - "use bs5 to make footer sticky" _Supposed to be_: "feat:use bs5 to make footer sticky"
- **3aa8e37** - "feat:add correct favion links & wire up html templates to navbar" _Supposed to be_: "feat:add correct favicon links & wire up html templates to navbar"
- **4f013c5** - "style:add my o css classes for styling of navbar and title" _Supposed to be_: "style:add my own css classes for styling of navbar and title"
- **522413b** - "docs:add validation of css and html" _Supposed to be_: "docs:add agile project board for user story/issues"

---

## Deployment

Please refer to the [DEPLOYMENT.md](/DEPLOYMENT.md) for all deployment documentation.

- The website was deployed on [Heroku](https://dashboard.heroku.com/apps)
- The database used was from the Code Institute Postgres database.
- Access [KUIDAORE](https://kuidaore-restaurant-3c1cdf981122.herokuapp.com/) here

---

### Credits
##### Content
  - I used [Chat GPT](https://chatgpt.com/) for generating text for each page.
  - I used [Stack Overflow](https://fontawesome.com/) for advice on how to get around problems with modals & BS5 issues.
  - I used [Font Awesome](https://fontawesome.com/) to create the icons used in the website.

##### Media
  - I used [ImageResizer](https://imageresizer.com/) for all the README.md, DEPLOYMENT.md, ERDDIAGRAM.md, WIREFRAMES.md and TESTING.md file images.
  - I used [Unsplash](https://unsplash.com/) for all the images used in the website.
  - I used [Chrome Capture Extension](https://chromewebstore.google.com/detail/chrome-capture-gif-screen/ggaabchcecdbomdcnbahdfddfikjmphe) for all the documentation images in the TESTING.md file.

## To do list
- Remove carousel after breakpoint, into gallery
- change mobile size nav bar
- testing for user stories / manual testing
- AUTOMATED / MANUAL TESTING