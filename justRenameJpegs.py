import os, sys, shutil

inpath = ""
fileList = []

if len(sys.argv)>=2:
	inpath=str(sys.argv[1])

def crawl_dir_get_list(inpath):
	filepath_list=[]
	for (path,dirs,files) in os.walk(inpath):
		for item in files:
			filepath=path+os.path.sep+item
			if filepath not in filepath_list:
				filepath_list.append(filepath)
	return sorted(filepath_list)

if inpath:
	print(inpath)
	fileList = crawl_dir_get_list(inpath)

if fileList:
	for item in fileList:
		if item.lower().endswith('.jpg'):
			itemSplit = item.split()
			itemSplitLength = len(itemSplit)
			if itemSplitLength > 1:
				print(itemSplit[1])
				newName = itemSplit[1]
				if not newName.lower().endswith('.jpg'):
					newName = newName+'.jpg'
				target = inpath+'/'+newName
				shutil.copyfile(item,target)
