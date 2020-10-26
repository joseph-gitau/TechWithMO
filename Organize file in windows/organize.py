import os

PATH = r"Enter Your Folder Path here"
files = os.listdir(PATH)
extensions = []

#get all the extension and store in extensions list
for f in files:
	main, extension = os.path.splitext(f)
	if extension not in extensions:
		extensions.append(extension)

#create folder named as extensions
for extension in extensions:
	if extension:
		os.mkdir(os.path.join(PATH, extension))

#move all files to their respective Folders
for i in files:
	main, extension = os.path.splitext(i)
	oldPath = os.path.join(PATH, i)
	newPath = os.path.join(PATH, extension, i)
	os.rename(oldPath, newPath)