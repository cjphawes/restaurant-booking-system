[&lt; Back to README file](/README.md)

# TESTING

The program was tested constantly throughout the development process. I had multiple users try out my game on multiple web browsers to spot bugs or grammatical mistakes which they found and I corrected, or noted down in the [Compatibility issues](#compatibility-section) section.

## Validation Testing

### Python Files
I used the Code Institute Python Linter to ensure sure the source code throughout was PEP8 compliant. The only errors were found in: 

-   Settings.py
-   

#### Home App
-   urls.py
![]()


## HTML Validation
The errors that were commonly thrown were:
    -   Any Django html template tags
    -   Top level elements not being present such as `head`, `lang=en`, `!DOCTYPE html` & `title`, but this was due to me using Django html templates.
    -   On update_reservation.html, the codes:
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

    However, despite this, my website ran smoothly with no major errors occurring.

## CSS Validation
No errors were found when passing it through the validator.
![W3C CSS Validation Image](/documentation/images/css-validation.webp)

## JS Validation
No errors were found when passing it through the validator
![JSHint Validation Image](/documentation/images/jshint-validation.webp)