#current_directory is the current path for your endnote library, which should be end with PDF, for example: 'G:....\XXX.Data\PDF'
#new_directory is the new path for all the pdf filess

def get_pdf(current_directory, new_directory):
	import os
	from shutil import copyfile
	deeper_directory = []
	deepest_directory = []
	for filename in os.listdir(current_directory):
		deeper_directory.append(filename)
	for item in deeper_directory:
		deepest_directory.append(current_directory+'\\'+item)
	for item in deepest_directory:
		for file in os.listdir(item):
			if file.endswith(".pdf"):
				copyfile(item+'\\'+file, new_directory+'\\'+file)

if __name__ == "__main__":
	path1 = input("please input current directory:")
	path2 = input("pleas input new directory")
	get_pdf(path1,path2)
