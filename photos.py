from photo import Photo

class Photos (object):
	def __init__ (self):
		self.photos = []
	def add(self, photo, al):
		f = 0
		for album in al.albums:
			if album.aname == photo.aname:
				self.photos.append(photo)
				f = 1
		if f == 0:
			print "album not found"
	def delete(self, pid):
		ind = -1
		index = -1
		for photo in self.photos:
			index += 1
			if pid == photo.pid:
				ind = index
		if ind > -1 : 		
			self.photos.pop(ind)

	def search(self, ph, form):
		i = -1
		for photo in self.photos:
			if form == photo.format:
				print photo
				i += 1
		if i == -1:
			print "photo with this format not found"
	def exists(self, aname):
		for photo in self.photos:
			if photo.aname == aname:
				return True
		return False
	
	def __str__ (self):
		for photo in self.photos:
			return '\n'.join(str(photo) for photo in self.photos)
