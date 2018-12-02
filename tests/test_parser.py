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

	def test_parser_accepts_xml(self):
		examp = ParseFile('''
			<document xmlns="http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml" version="1.0" producer="languages=" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.abbyy.comFineReader_xml/FineReader10-schema-v1.xml http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml">
				<page width="2555" height="3532" resolution="300" originalCoords="1">
					<block blockType="Text" l="184" t="156" r="249" b="3105">
						<region>
							<rect l="184" t="156" r="246" b="591"/>
							<rect l="184" t="591" r="247" b="600"/>
						</region>
						<text>
							<par leftIndent="900" lineSpacing="1330">
								<line baseline="3099" l="194" t="3069" r="237" b="3099">
									<formatting lang="EnglishUnitedStates" ff="Times New Roman" fs="9.5" bold="1" spacin="20">
										25
									</formatting>
								</line>
							</par>
						</text>
					</block>
				</page>
			</document>''')
		self.assertIsInstance(list, type(examp))

