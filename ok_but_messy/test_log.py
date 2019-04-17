import time

class delete_Log(object):
	def __init__(self, path = '', mode = 'w'):
		file_name = 'create_log: ' + time.strftime('%m-%d-%y-%H-%M-%S', time.localtime())
		self.log = open(path + file_name + '.txt', mode)

	def log_write(self,msg):
		self.log.write(msg)

	def log_close(self):
		self.log.close()


class edit_Info(object):
	def __init__(self, path = '', mode = 'w'):
		file_name = 'edit_log: ' + time.strftime('%m-%d-%y-%H-%M-%S', time.localtime())
		self.log = open(path + file_name + '.txt', mode)

	def log_write(self,msg):
		self.log.write(msg)

	def log_close(self):
		self.log.close()

class delete_Log(object):
	def __init__(self, path = '', mode = 'w'):
		file_name = 'delete_log: ' + time.strftime('%m-%d-%y-%H-%M-%S', time.localtime())
		self.log = open(path + file_name + '.txt', mode)

	def log_write(self,msg):
		self.log.write(msg)

	def log_close(self):
		self.log.close()

if __name__ == '__main__':
	log = Log_info()
	log.log_write('test_log')
	log.log_close()