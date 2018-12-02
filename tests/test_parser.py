import os
import unittest

from parser import app
from parser.fileParser import ParseFile


class Tests(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		self.app = app.test_client()
		
	def test_home_page_available(self):
		home_page = self.app.get('/')
		self.assertEqual(home_page.status, '200 OK')
