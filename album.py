class Album(object):
	def __init__(self, aid, aname, cr_dat):
		self.aid = aid;
		self.aname = aname
		self.cr_dat = cr_dat
	def __str__(self):
		return "%d	%s	%s" % (self.aid, self.aname, self.cr_dat)

	
	
	