class Photo(object):
	def __init__(self, pid, pname, format, aname):
		self.pid = pid;
		self.pname = pname
		self.format = format
		self.aname = aname
	def __str__(self):
			return "%d	%s	%s	%s" % (self.pid, self.pname, self.format, self.aname)

	
	
	