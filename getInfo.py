def get_webinfo(webinfo_path):
	webinfo_dict = {}
	config = open(webinfo_path)
	for line in config:
		pairs = [ele.strip() for ele in line.split('=')]
		webinfo_dict[pairs[0]]= pairs[1]
	
	return webinfo_dict



def get_id(id_path):
	config = open(id_path)
	id_list = [line.rstrip('\n') for line in config]

	return id_list