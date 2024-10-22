from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Reservation, Review
from datetime import datetime


class ViewTests(TestCase):
    # Setup the fake user & reservation
    def setUp(self):
        self.user = User.objects.create_superuser(
                username="myUsername",
                password="myPassword",
                email="test@test.com"
        )
        self.reservation = Reservation.objects.create(
            customer=self.user, name='Joe Bloggs',
            reservation_date='2024-11-01',
            reservation_time=datetime.strptime('18:00', '%H:%M').time(),
            number_of_guests=4
        )
        self.client.login(username="testusername", password="123456789")

    # Testing for the correct status code and user
    def test_list_reservations(self):
        self.client.login(username="testusername", password="123456789")
        response = self.client.get(reverse('reservationDetails'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Joe Bloggs')

    #  Test for correct redirection and form posting
    def test_update_reservation(self):
        response = self.client.post(reverse('reservationUpdate',
                                            args=[self.reservation.id]), {
            "date": "2024-12-13",
            "time": "19:30",
            "num_of_guests": 10
        })
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.reservation_date,
                         datetime.strptime('2024-12-13', '%Y-%m-%d').date())
        self.assertEqual(self.reservation.reservation_time,
                         datetime.strptime('19:30', '%H:%M').time())
        self.assertEqual(self.reservation.number_of_guests, 10)

    def test_remove_reservation(self):
        response = self.client.post(reverse('reservationRemove',
                                            args=[self.reservation.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 0)

    def test_leave_review(self):
        response = self.client.post(reverse('submit_review'), {
            "name": "John Smith",
            "subject": "Testing a review",
            "content": "This is a test to see if the form posts"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.reviewer_name, 'John Smith')

    def make_reservation(self):
        response = self.client.post(reverse('reservationForm')), {
            'name': "John Doe",
            'num_of_guests': 8,
            'date': "2024-11-23",
            'time': "18:30"
        }
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 2)
        new_reservation = Reservation.objects.last()
        self.assertEqual(new_reservation.name, "John Doe")
