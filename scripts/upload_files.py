import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from time import sleep

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

timestring = time.strftime("%Y%m%d-%H%M")

upload_file_list = ['Secrets.kdbx']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'title': [upload_file[:7] + timestring + "." + upload_file[-4:]],
	'parents': [{'id': '1Ln6ptJ4bTlYoGdxczIgmD-7xcRlJa_7m'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1Ln6ptJ4bTlYoGdxczIgmD-7xcRlJa_7m')}).GetList()
for file in file_list:
	print('title: %s, id: %s' % (file['title'], file['id']))

# Download the files from Google Drive

# for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
# 	print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
# 	file.GetContentFile(file['title'])

sleep(10)
