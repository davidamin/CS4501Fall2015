from django.test import TestCase
from django.test import Client
from .models import User, Vehicle, Ride
import json

class UserTestCases(TestCase):
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create(username='TP', first='T', last='P', email='tp@mail.com', password='password', city='Charlottesville', state='VA', phone_number='1234567890', payment_type=1, gender=True, age=25)

	def tearDown(self):
		self.user1.delete()		

	def test_NewUser(self):

		response = self.client.post('/models/add_user', {'username': 'abc', 'first': 'a', 'last':'c', 'email':'test@mail.com', 'password': 'password', 'city': 'Charlottesville', 'state': 'VA', 'phone': '2024060100', 'payment_type': '1', 'gender': 'True', 'age':'20'})
		
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'User Created')

		user = User.objects.get(username="abc")
		self.assertTrue(user)

	#Fails for user #1
	def test_GetUser(self):
		self.client.post('/models/add_user', {'username': 'TPI', 'first': 'a', 'last':'c', 'email':'test@mail.com', 'password': 'password', 'city': 'Charlottesville', 'state': 'VA', 'phone': '2024060100', 'payment_type': '1', 'gender': 'True', 'age':'20'})

		response = self.client.get('/models/get_user/5')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'true')
		self.assertContains(response, 'TP')

		response2 = self.client.get('/models/get_user/6')

		self.assertEqual(response2.status_code, 200) 
		self.assertContains(response2, 'true')
		self.assertContains(response2, 'TPI')

	def test_GetUserByName(self):
		#response = self.client.post('/models/add_user', {'username': 'abc', 'first': 'a', 'last':'c', 'email':'test@mail.com', 'password': 'password', 'city': 'Charlottesville', 'state': 'VA', 'phone': '2024060100', 'payment_type': '1', 'gender': 'True', 'age':'20'})

		response = self.client.get('/models/get_user_by_name/', {'user': 'abc'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'abc')

	def test_DeactivateUser(self):
		response = self.client.post('/models/deactivate_user/4', {'deactivate': '1', 'user': '1'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Deactivated")

class VehicleTestCases(TestCase):
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create(username='TP', first='T', last='P', email='tp@mail.com', password='password', city='Charlottesville', state='VA', phone_number='1234567890', payment_type=1, gender=True, age=25)
		self.vehicle1 = Vehicle.objects.create(max_seats=5, trunk_space=3, notes='None', make='Tesla', model='Model S', year='2015', color='Red', plates='ELCTRC', road_assistance='None', accomodations='None')
		self.vehicle2 = Vehicle.objects.create(max_seats=5, trunk_space=3, notes='None', make='Tesla', model='Model S', year='2015', color='Red', plates='ELCTRIC', road_assistance='None', accomodations='None')

	def tearDown(self):
		self.user1.delete()
		self.vehicle1.delete()
		self.vehicle2.delete()

	def test_NewVehicle(self):
		response = self.client.post('/models/add_vehicle', {'username': 'TP', 'max_seats': '5', 'trunk_space': '2', 'notes': 'NA', 'make': 'Acura', 'model':'Integra', 'year': '1999', 'color': 'white', 'plates': 'XMG7842', 'accomodations': 'None', 'road_assistance': 'None'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Added vehicle")

		vehicle = Vehicle.objects.get(pk=8)
		self.assertEqual(vehicle.plates, 'XMG7842')

	def test_GetCar(self):
		response = self.client.get('/models/get_car/4', {'car': '1'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'true')
		self.assertContains(response, 'ELCTRC')


class RideTestCases(TestCase):
	def setUp(self):
		self.client = Client()
		self.vehicle1 = Vehicle.objects.create(max_seats=5, trunk_space=3, notes='None', make='Tesla', model='Model S', year='2015', color='Red', plates='ELCTRC', road_assistance='None', accomodations='None')
		self.user1 = User.objects.create(username='TP', first='T', last='P', email='tp@mail.com', password='password', city='Charlottesville', state='VA', phone_number='1234567890', payment_type=1, gender=True, age=25, vehicle=self.vehicle1)
		#self.ride1 = Ride.objects.create(leave_time='09:30', arrive_time='11:30', destination='Charlottesville', start='Fairfax', comments='None', max_miles_offroute=15, driver=self.user1)
		#self.ride2 = Ride.objects.create(leave_time='12:30', arrive_time='02:30', destination='Fairfax', start='Charlottesville', comments='None', max_miles_offroute=15, driver=self.user1)

	def tearDown(self):
		self.user1.delete()
		self.vehicle1.delete()
		#self.ride1.delete
		#self.ride2.delete

	def test_NewRide(self):
		response = self.client.post('/models/add_ride', {'leave_time':'05:00', 'arrive_time':'10:00', 'destination': 'NYC', 'start':'Fairfax', 'comments': 'None', 'max_miles_offroute': '15', 'username':'TP'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Ride Created")

	def test_GetRide(self):
		self.client.post('/models/add_ride', {'leave_time':'12:00', 'arrive_time':'05:00', 'destination': 'Fairfax', 'start':'NYC', 'comments': 'None', 'max_miles_offroute': '15', 'username':'TP'})

		response = self.client.get('/models/get_ride/2')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'true')

	def test_DeactivateRide(self):
		self.client.post('/models/add_ride', {'leave_time':'12:00', 'arrive_time':'05:00', 'destination': 'Fairfax', 'start':'NYC', 'comments': 'None', 'max_miles_offroute': '15', 'username':'TP'})
		response = self.client.post('/models/deactivate_ride/1', {'deactivate': '1'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Deactivated')

# Create your tests here.