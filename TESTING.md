[&lt; Back to README file](/README.md)

# TESTING

The project was tested constantly throughout the development process. I had multiple users try out my website on multiple web browsers to spot bugs or grammatical mistakes which they found and I corrected.

## Validation Testing

### Python Validation
I used the Code Institute Python Linter to ensure sure the source code throughout was PEP8 compliant. The only errors were found in: 

-   Kuidaore/Settings.py - due to not being able to shorten the length of objects
![PEP8 Validation 1](/documentation/images/pep8-validation-1.webp)
-   Reservations/Views.py - due to not being able to shorten the length of the if statement
![PEP8 Validation 2](/documentation/images/pep8-validation-2.webp)

### HTML Validation
The errors that were commonly thrown were:
-   Any Django html template tags
-   Top level elements not being present such as `head`, `lang=en`, `!DOCTYPE html` & `title`, but this was due to me using Django html templates.
-   On `update_reservation.html`, the code is as shown:

    ```
        <option value="17:00" {% if reservation.reservation_time|date:"H:i" == "17:00" %}selected{% endif %}>17:00</option>
        <option value="17:30" {% if reservation.reservation_time|date:"H:i" == "17:30" %}selected{% endif %}>17:30</option>
        <option value="18:00" {% if reservation.reservation_time|date:"H:i" == "18:00" %}selected{% endif %}>18:00</option>
        <option value="18:30" {% if reservation.reservation_time|date:"H:i" == "18:30" %}selected{% endif %}>18:30</option>
        <option value="19:00" {% if reservation.reservation_time|date:"H:i" == "19:00" %}selected{% endif %}>19:00</option>
        <option value="19:30" {% if reservation.reservation_time|date:"H:i" == "19:30" %}selected{% endif %}>19:30</option>
        <option value="20:00" {% if reservation.reservation_time|date:"H:i" == "20:00" %}selected{% endif %}>20:00</option>
        <option value="20:30" {% if reservation.reservation_time|date:"H:i" == "20:30" %}selected{% endif %}>20:30</option>
        <option value="21:00" {% if reservation.reservation_time|date:"H:i" == "21:00" %}selected{% endif %}>21:00</option>
        <option value="21:30" {% if reservation.reservation_time|date:"H:i" == "21:30" %}selected{% endif %}>21:30</option>
        <option value="22:00" {% if reservation.reservation_time|date:"H:i" == "22:00" %}selected{% endif %}>22:00</option>
        <option value="22:30" {% if reservation.reservation_time|date:"H:i" == "22:30" %}selected{% endif %}>22:30</option>
        <option value="23:00" {% if reservation.reservation_time|date:"H:i" == "23:00" %}selected{% endif %}>23:00</option>
    ```
    and
    ```
        <option value="1" {% if reservation.number_of_guests == 1 %}selected{% endif %}>1</option>
        <option value="2" {% if reservation.number_of_guests == 2 %}selected{% endif %}>2</option>
        <option value="3" {% if reservation.number_of_guests == 3 %}selected{% endif %}>3</option>
        <option value="4" {% if reservation.number_of_guests == 4 %}selected{% endif %}>4</option>
        <option value="5" {% if reservation.number_of_guests == 5 %}selected{% endif %}>5</option>
        <option value="6" {% if reservation.number_of_guests == 6 %}selected{% endif %}>6</option>
        <option value="7" {% if reservation.number_of_guests == 7 %}selected{% endif %}>7</option>
        <option value="8" {% if reservation.number_of_guests == 8 %}selected{% endif %}>8</option>
        <option value="9" {% if reservation.number_of_guests == 9 %}selected{% endif %}>9</option>
        <option value="10" {% if reservation.number_of_guests == 10 %}selected{% endif %}>10</option>
    ```
    threw up errors with the equal signs and the quotation marks inside the if tag.

    However, despite this, my website ran smoothly with no errors occurring and functionality working as it should.

### CSS Validation
No errors were found when passing it through the validator.
![W3C CSS Validation Image](/documentation/images/css-validation.webp)

### JS Validation
No errors were found when passing it through the validator
![JSHint Validation Image](/documentation/images/jshint-validation.webp)

## Manual Testing

- Be aware! On some of the evidence below, when using the modal, the screen capture doesn't show the modal elements showing.

| ID No. | Action | Testing | Result | Evidence |
|--------|--------|---------|--------|----------|
| **1** | Click carousel arrows to change images | Clicks arrow | The image changes to a different one | ![Change Carousel Images](/documentation/gifs/change-carousel-img.gif) |
| **2** | Navigate to the Menu page from the home page | Click the menu button | The webpage changes to the Menu page | ![Go to Menu Page from home page](/documentation/gifs/navigate-to-menu-page-btn.gif) |
| **3** | Navigate to the Reservations page from the home page | Click the reservations button | The webpage changes to the Reservations page | ![Go to reservations page from home page](/documentation/gifs/navigate-to-reservations-btn.gif) |
| **4** | Navigate to the Contact page from the home page | Click the contact button | The webpage changes to the Contact page | ![Go to contact page from home page](/documentation/gifs/navigate-to-contact-btn.gif) |
| **5** | Redirect back to the Home page | Click on the logo | The webpage redirects the user to the home page | ![Redirect to home page](/documentation/gifs/redirect-to-landing-page-logo.gif) |
| **6** | Display the Wine & Sake menu | Click on the button | A modal appears displaying the Wine & Sake menu | ![Open Menu page modal](/documentation/gifs/open-wine-sake-modal.gif) |
| **7** | Navigate to the Reservations page from the About page | Click on the Make a reservation button | The webpage will change to the reservations page | ![Navigate to reservation page from about page](/documentation/gifs/about-page-reservations-btn.gif) |
| **8** | Navigate to the Contact page from the About page | Click on the Contact us button | The webpage will change to the Contact page | ![Navigate to contact page from about page](/documentation/gifs/about-page-contact-btn.gif) |
| **9** | Navigate to the Contact page from the FAQ page | Click on the Contact us button | The webpage will change to the Contact page | ![Navigate to contact page from FAQ page](/documentation/gifs/faq-page-contact-btn.gif) |
| **10** | View an FAQ | Click on a FAQ to view | The selected FAQ will display a dropdown, providing information about that question | ![View an FAQ](/documentation/gifs/view-faqs.gif) |
| **11** | When logged in, navigate to the review form | Click on the leave a review button | The webpage changes to the review form | ![Navigate to review form from contact page](/documentation/gifs/contact-page-review-btn.gif) |
| **12** | Try to log in | Click on the log in button to show the modal, then click the log in link | The webpage changes to the sign-in form | ![Go to Login page](/documentation/gifs/navigate-to-login-page.gif) |
| **13** | Try to register | Click on the log in button to show the modal, then click the register link | The webpage changes to the register form | ![Go to register page](/documentation/gifs/navigate-to-register-page.gif) |
| **14** | Try to log in from register form | Click on the Sign-in button | The webpage changes to the sign-in form | ![Go to login page from register page](/documentation/gifs/register-page-login-btn.gif) |
| **15** | Try to register from sign in form | Click on the Sign-up button | The webpage changes to the sign-up form | ![Go to register page from login page](/documentation/gifs/login-page-register-btn.gif) |
| **16** | Create an account | Input details and click the Sign-up button | The webpage changes to the home page and "Log in" changes to "Log out" | ![Create an account](/documentation/gifs/create-an-account.gif) |
| **17** | Signing in | Input details and click the Sign-in button | The webpage changes to the home page and "Log in" changes to "Log out" | ![Login to account](/documentation/gifs/login-to-account.gif) |
| **18** | Logging out | Click the log out button in the navigation bar | A modal will show asking user to confirm, this will then take you to the sign out form | ![Go to logout page](/documentation/gifs/navigate-to-logout-page.gif) |
| **19** | Confirming Log out | Click the sign-out button | The webpage changes to the home page and "Log out" changes back to "Log in" | ![Confirming logout of user](/documentation/gifs/confirming-logout.gif) |
| **20** | Navigate to the register or log in forms from the reservations page | Click on either button respectively | The webpage changes to the respective form | ![Navigate to authentication pages from reservation page](/documentation/gifs/reservations-page-authentication-btns.gif) |
| **21** | Make a reservation | Click on the "Make a reservation" button | A reseravtion modal shows allowing the user to input details and confirming with a button and a success message | ![Make a reservation](/documentation/gifs/making-a-reservation.gif) |
| **22** | View your reservations | If logged in, click on "View your reservations" | The webpage will change to display your reservations page | ![View a reservaiton](/documentation/gifs/view-user-reservations.gif) |
| **23** | Cancel a reservation | Navigate to the cancel form and click the "cancel" button | This takes you to another webpage where you can confirm your cancellation | ![Cancel a reservation](/documentation/gifs/cancel-user-reservation.gif) |
| **24** | Modify a reservation | Navigate to the modify form and click the "modify" button | This takes you to another webpage giving you the same reservation form to adjust your details and confirm the modification | ![Modift a reservation](/documentation/gifs/modify-user-reservation.gif) |

## User Story Testing

| Action | Requirements Met | Evidence |
|--------|------------------|----------|
| As a user I can reserve a time slot dictating the number of guests I would like attending so that I can visit this restaurant with a certain number of friends | Y | ![]() |
| As a user I can navigate the website easily so that I am able to find all the necessary requirements I need to create a reservation or leave a review | Y | ![]() |
| As a user I can send a cancellation for a reservation so that my reservations are always up to date with the correct information | Y | ![]() |
| As a user I can get answers to any questions or queries I may have so that I can make an informed decision whether or not I want to visit the restaurant | Y | ![]() |
| As a user I can register an account with the restaurant so that my details are saved for ease of reservations the next time I intend to visit | Y | ![]() |
| As a user I can change the preferred language of the website so that I am able to go through the website and understand it in my own language | N | **Implemented in Future Feature** |
| As a user I can view the menu before attending so that I can decide what food I would like to eat | Y | ![]() |
| As a user I can review and send a feedback form to the restaurant so that I can provide constructive criticism to improve their website or restaurant | Partially Completed | ![]() |
| As a user I can sign-up to the restaurants newsletter so that I can receive information about promotions or any news/events | N | **Implemented in Future Feature** |

## Lighthouse Dev Tools
I used the Lighthouse Dev Tools to assess the performance and accessibility of my website.
![Lighthouse Dev Tool](/documentation/images)

[&lt; Back to README file](/README.md)