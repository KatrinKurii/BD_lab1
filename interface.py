from albums import Albums
from photos import Photos
from album import Album
from photo import Photo
class Interface (object):
	def menu():
		print "1. ADD "
		print "2. DELETE "
		print "3. REVIEW "
		print "4. SEARCH PHOTOS BY FORMAT BMP"
		print "5. EXIT "
		selection = raw_input()
		print "1. PHOTOS "
		print "2. ALBUMS "
		list_num  = raw_input()
		if selection == '1' and list_num == '1':
			pid = len(ph.photos)
			pname = raw_input("pname = ")
			format = raw_input("format = ")
			aid = int(raw_input("aid = "))
			photo0 = Photo(pid, pname, format, aid)
			photos.add(photo0,al)
		elif selection == '1' and list_num == '2':
			aid = len(al.albums)
			aname = raw_input("aname = ")
			cr_dat = raw_input("cr_dat = ")
			album0 = Album(aid, aname, cr_dat)
			albums.add(album0)
		elif selection == '2' and list_num == '1':
			ph_num = int(raw_input("what photo you want delete:"))
			photos.delete(ph_num)
		elif selection == '2' and list_num == '2':
			al_num = int(raw_input("what album you want delete:"))
			albums.delete(al_num)
		elif selection == '3' and list_num == '1':
			print (" photos:")
			print photos
		elif selection == '3' and list_num == '2':
			print (" albums:")
			print albums
		elif selection == '4':
			print (" photo bmp:")
			photos.search(ph,'bmp')
		elif selection == '5':
			return 0
		else:
			menu()
			return
