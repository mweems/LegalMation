from xml.etree import cElementTree as ET
import re

PLAINTREGS = [
	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 	re.compile('-- --+Plaintiff (\w* \w*)'),
 ]

DEFENDANTREGS = [
	re.compile('vs.-- --(.*)Defendants'),
 	re.compile('-- --v(.*) --Defendants'),
 ]

def ParseFile(file):
	tree = ET.parse(file)
	root = tree.getroot()
	data = "-- --".join(root.itertext()).replace("\n", '')

	results = {}

	results['plaintiffs'] = GetPlaintiffs(data)
	results['defendants'] = GetDefendants(data)

	return results


def GetPlaintiffs(data):
	plaintiffs = []
	
	for item in PLAINTREGS:
		match = item.search(data)
		if match:
			plaintiffs.append(match.group(1).replace("-- --", ''))

	return plaintiffs


def GetDefendants(data):
	defendants = []

	for item in DEFENDANTREGS:
		match = item.search(data)
		if match:
			defendants.append(match.group(1).replace("-- --", ''))

	return defendants



