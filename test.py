from album import Album
from albums import Albums
from photo import Photo
from photos import Photos
import pickle
def menu():
	print "1. ADD "
	print "2. DELETE "
	print "3. DISPLAY "
	print "4. SEARCH PHOTOS BY FORMAT BMP"
	print "5. EXIT "
	selection = raw_input()
	if selection != '4' and selection != '5':
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
		albums.delete(al_num,ph)
	elif selection == '3' and list_num == '1':
		print (" photos:")
		if len(ph.photos) != 0:
			print photos
		else: print "empty"
	elif selection == '3' and list_num == '2':
		print (" albums:")
		if len(al.albums) != 0:
			print albums
		else: print "empty"
	elif selection == '4':
		print (" photo bmp:")
		photos.search(ph,'bmp')
	elif selection == '5':
		return 0
	else:
		menu()
		return
	menu()

dbfile = "dbfile.dat"
photos = Photos()
albums = Albums()

with open(dbfile,"rb") as file:
	photos = pickle.load(file)
	albums = pickle.load(file)
	
#album1 = Album(0, 'A', '11/9/2017')
#album2 = Album(1, 'B', '10/9/2017')
#album3 = Album(2, 'C', '21/9/2017')
#albums.add(album1)
#albums.add(album2)
#albums.add(album3)
al = albums

#photo1 = Photo(0, 'aaa', 'jpg', 'B')
#photo2 = Photo(1, 'bbb', 'bmp', 'A')
#photo3 = Photo(2, 'ccc', 'bmp', 'C')
#photo4 = Photo(3, 'ddd', 'jpg', 'B')
#photo5 = Photo(4, 'eee', 'bmp', 'A')
#photos.add(photo1,al)
#photos.add(photo2,al)
#photos.add(photo3,al)
#photos.add(photo4,al)
#photos.add(photo5,al)
ph = photos
menu()

#photos = Photos()
#albums = Albums()
with open(dbfile, "wb") as file:
	pickle.dump(photos, file)
	pickle.dump(albums, file)




