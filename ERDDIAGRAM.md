[&lt; Back to README file](/README.md)

# ERD Diagram

- PostgreSQL was used for the database.

![ERD diagram of database](/documentation/images/kuidaore-erd-diagram.webp)

### Review Model

| Key | Field Type | Validation | 
|-----|------------|------------|
| reviewer_email | CharField | max_length=150 |
| subject | CharField | max_length=250 |
| review_date | DateField | auto_now_add=True |
| review_content | TextField |  |

### Reservation Model

| Key | Field Type | Validation | 
|-----|------------|------------|
| customer | ForeignKey | User, on_delete=models.CASCADE, related_name="client_name" |
| name | CharField | max_length=150 |
| reservation_time | TimeField |  |
| reservation_date | DateField |  |
| number_of_guests | Integer | default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)] |

_Note_: I used Min & Max Validators for the "number_of_guests" key to make sure a positive number was used and 0 couldn't be input by the user.
