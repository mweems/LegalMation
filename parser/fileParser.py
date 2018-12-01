import xml.etree.ElementTree as ET


def ParseFile(file):
	tree = ET.parse(file)
	root = tree.getroot()
	return root