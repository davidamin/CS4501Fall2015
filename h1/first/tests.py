from django.test import TestCase
from django.test import Client
from .models import User
import json

class UserTestCases(TestCase):
	def setUp(self):
		self.client = Client()

	def test_NewUser(self):

		response = self.client.post('/models/add_user', {'username': 'abc', 'first': 'a', 'last':'c', 'email':'test@mail.com', 'password': 'password', 'city': 'Charlottesville', 'state': 'VA', 'phone': '2024060100', 'payment_type': '1', 'gender': 'True', 'age':'20'})
		
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'User Created')

		user = User.objects.get(username="abc")
		self.assertTrue(user)

		user2 = User.objects.get(pk=1)
		self.assertEqual(user2.username, 'abc')

	#Failing despite the correct user ID not being found (based off of test_NewUser)
	def test_GetUser(self):
		
		response = self.client.get('/models/get_user/1')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Failed')

	def test_GetUserByName(self):
		#response = self.client.post('/models/add_user', {'username': 'abc', 'first': 'a', 'last':'c', 'email':'test@mail.com', 'password': 'password', 'city': 'Charlottesville', 'state': 'VA', 'phone': '2024060100', 'payment_type': '1', 'gender': 'True', 'age':'20'})

		response = self.client.get('/models/get_user_by_name/', {'user': 'abc'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'abc')

	#Failing despite the correct user ID not being found (Correct user ID is based off of test_NewUser)
	def test_DeactivateUser(self):
		response = self.client.post('/models/deactivate_user/1', {'deactivate': '1', 'user': 1})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, " Deactivated ")

class VehicleTestCases(TestCase):
	def setUp(self):
		self.client = Client()
# Create your tests here.
