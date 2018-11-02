from service import Service
from unittest import TestCase
from mock import patch
import sys

class TestService(TestCase):
	@patch('service.Service.bad_random', return_value=10)
	def test_bad_random(self, bad_random):
		self.assertEqual(bad_random(), 10)

	@patch('service.Service.bad_random', return_value=10)
	def test_divide(self, bad_random):
		x = Service()
		self.assertEqual(x.divide(2),5) 
		self.assertEqual(x.divide(-2),-5)
		
		bad_random.return_value=-10
		self.assertEqual(x.divide(2),-5)
		
		bad_random.return_value=0
		self.assertEqual(x.divide(sys.maxsize),0)
		self.assertEqual(x.divide(-sys.maxsize+1),0)


	def test_abs_plus(self):
		x=Service()
		self.assertEqual(x.abs_plus(10),11)
		self.assertEqual(x.abs_plus(0),1)
		self.assertEqual(x.abs_plus(-10),11)
		self.assertEqual(x.abs_plus(-sys.maxsize+1),sys.maxsize)
		self.assertEqual(x.abs_plus(10),11)

	@patch('service.Service.bad_random', return_value=10)
	def test_complicated_function(self, bad_random):

		x = Service()
		results = x.complicated_function(20)
		self.assertEqual(results[0], 0.5)
		self.assertEqual(results[1], 0)
		
		bad_random.return_value=-13
		results = x.complicated_function(-1)
		self.assertEqual(results[0], 13)
		self.assertEqual(results[1], 1)
		
		bad_random.return_value=0
		results = x.complicated_function(sys.maxsize)
		self.assertEqual(results[0], 0)
		self.assertEqual(results[1], 0)
		