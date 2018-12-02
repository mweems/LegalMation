import xmltodict

def ParseFile(file):
	data = xmltodict.parse(file)
	return data