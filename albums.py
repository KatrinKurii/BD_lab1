from album import Album
from photos import Photos

class Albums (object):
	def __init__ (self):
		self.albums = []
	def add(self, album):
		self.albums.append(album)
	def delete(self, aid, ph):
		ind = -1
		index = -1
		for album in self.albums:
			index += 1
			if aid == album.aid:
				ind = index
				a_name = album.aname
		if ind > -1 :
			while ph.exists(a_name):
				indf = -1
				i = -1
				for photo in ph.photos:
					i +=1
					if a_name == photo.aname:
						indf = i
						break
				if indf>-1:
					ph.photos.pop(indf)
			self.albums.pop(ind)
		
		
	def __str__ (self):
		for album in self.albums:
			return '\n'.join(str(album) for album in self.albums)