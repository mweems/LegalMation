from xml.etree import cElementTree as ET
import re

PLAINTREGS = [
	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 ]

DEFENDANTREGS = [
	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 	re.compile('.*\w-- --(.+)(-- --)+Plaintiff'),
 ]


def ParseFile(file):
	tree = ET.parse(file)
	root = tree.getroot()
	data = "-- --".join(root.itertext())

	results = {}

	results['plaintiffs'] = GetPlaintiffs(data)
	results['defendants'] = GetDefendants(data)

	return results


def GetPlaintiffs(data):
	plaintiffs = []
	
	for item in PLAINTREGS:
		match = item.match(data.replace("\n", ""))
		plaintiffs.append(match.group(1).replace("-- --", ''))

	return plaintiffs


def GetDefendants(data):
	defendants = []

	for item in DEFENDANTREGS:
		match = item.match(data.replace("\n", ""))
		defendants.append(match.group(1).replace("-- --", ''))

	return defendants



