import xmltodict

def ParseFile(file):
	data = dict(dict(xmltodict.parse(file))['document'])['page']['block']
	return type(data)