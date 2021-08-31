from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='yazan',
            email='yazan-ahmed1999a@outlook.com',
            password='0770181800'
        )
        self.snack = Snack.objects.create(
            title='burger',
            purshaser=self.user,
            description='A hamburger is a food, typically considered a sandwich, consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bread roll or bun. The patty may be pan fried, grilled, smoked or flame broiled.'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "burger")


    def test_thing_content(self):
        self.assertEqual(self.snack.title, 'burger')
        self.assertEqual(str(self.snack.purshaser), 'yazan')
        self.assertEqual(self.snack.description, 'A hamburger is a food, typically considered a sandwich, consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bread roll or bun. The patty may be pan fried, grilled, smoked or flame broiled.')


    def test_snack_list_view(self):
        expected = 200
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, expected)
        self.assertContains(response, "burger")
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack_details_view(self):
        expected = 200
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/800/")
        self.assertEqual(response.status_code, expected)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "burger")
        self.assertTemplateUsed(response, "snack_detail.html")


    def test_snack_create_view(self):
        expected = 200
        actual = self.client.post(reverse('create_snack'),{'title': 'burger', ' purshaser': self.user,'description': 'A hamburger is a food',})
        self.assertEqual(expected, actual.status_code)
        self.assertContains(actual, 'A hamburger is a food')
        self.assertContains(actual, 'yazan')


    def test_snack_update_view(self):
        expected = 200
        actual = self.client.post(reverse('update_snack', args='1')).status_code
        self.assertEqual(expected, actual)


    def test_snack_delete_view(self):
        expected = 200
        actual = self.client.get(reverse('delete_snack', args='1')).status_code
        self.assertEqual(expected, actual)

