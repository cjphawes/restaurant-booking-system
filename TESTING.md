[&lt; Back to README file](/README.md)

# TESTING

The program was tested constantly throughout the development process. I had multiple users try out my game on multiple web browsers to spot bugs or grammatical mistakes which they found and I corrected, or noted down in the [Compatibility issues](#compatibility-issues) section.

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

| Action | Testing | Result | Evidence |
|--------|---------|--------|----------|
| Click carousel arrows to change images | Clicks arrow | The image changes to a different one | ![]() |
| Navigate to the Menu page from the home page | Click the menu button | The webpage changes to the Menu page | ![]() |
| Navigate to the Reservations page from the home page | Click the reservations button | The webpage changes to the Reservations page | ![]() |
| Navigate to the Contact page from the home page | Click the contact button | The webpage changes to the Contact page | ![]() |
| Redirect back to the Home page | Click on the logo | The webpage redirects the user to the home page | ![]() |
| Display the Wine & Sake menu | Click on the button | A modal appears displaying the Wine & Sake menu | ![]() |
| Navigate to the Reservations page from the About page | Click on the Make a reservation button | The webpage will change to the reservations page | ![]() |
| Navigate to the Contact page from the About page | Click on the Contact us button | The webpage will change to the Contact page | ![]() |
| Navigate to the Contact page from the FAQ page | Click on the Contact us button | The webpage will change to the Contact page | ![]() |
| View an FAQ | Click on a FAQ to view | The selected FAQ will display a dropdown, providing information about that question | ![]() |
| When logged in, navigate to the review form | Click on the leave a review button | The webpage changes to the review form | ![]() |
| Try to log in | Click on the log in button to show the modal, then click the log in link | The webpage changes to the sign-in form | ![]() |
| Try to register | Click on the log in button to show the modal, then click the register link | The webpage changes to the register form | ![]() |
| Try to log in from register form | Click on the Sign-in button | The webpage changes to the sign-in form | ![]() |
| Try to register from sign in form | Click on the Sign-up button | The webpage changes to the sign-up form | ![]() |
| Create an account | Input details and click the Sign-up button | The webpage changes to the home page and "Log in" changes to "Log out" | ![]() |
| Signing in | Input details and click the Sign-in button | The webpage changes to the home page and "Log in" changes to "Log out" | ![]() |
| Logging out | Click the log out button in the navigation bar | A modal will show asking user to confirm, this will then take you to the sign out form | ![]() |
| Confirming Log out | Click the sign-out button | The webpage changes to the home page and "Log out" changes back to "Log in" | ![]() |
| Navigate to the register or log in forms from the reservations page | Click on either button respectively | The webpage changes to the respective form | ![]() |
| Make a reservation | Click on the "Make a reservation" button | A reseravtion modal shows allowing the user to input details and confirming with a button and a success message | ![]() |
| View your reservations | If logged in, click on "View your reservations" | The webpage will change to display your reservations page | ![]() |
| Cancel a reservation | Click the "cancel" button | This takes you to another webpage where you can confirm your cancellation | ![]() |
| Modify a reservation | Click the "modify" button | This takes you to another webpage giving you the same reservation form to adjust your details and confirm the modification | ![]() |




### Compatibility Issues