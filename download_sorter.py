import os
import glob
import shutil

# key of the map is the directory that the file is put in
extensions = { 
	'Pictures' : [
		'jpeg', 'jpg', 'gif', 'png'
],
	'Archive' : [
		'tar', 'bz2', 'gz', 'zip'
],

	'Documents' : [
		'txt', 'odt', 'pdf'
],
	'WebDocuments' : [
		'xml', 'html'
]}

dwnld = os.path.normpath('/home/liam/Downloads/bak/')
dwnld2  = os.path.normpath('/home/liam/')
user_path = os.path.normpath('/bome/liam')
if (os.path.exists(dwnld)):
	for key in extensions:
		#print key
		for extension in extensions[key]:
		#	print dwnld + '/*.' + extension
			for file_name in glob.glob(dwnld + '/*.' + extension): 	
				print 'Moving ' + file_name  + ' to' + dwnld2+ '/' + key
				shutil.copy(file_name,  os.path.join(dwnld2 + '/' + key))	

else:
	print 'Failed to open: ' + dwnld + '\n'
	dnwld = os.path.normpath(raw_input('Enter a new directory'))

