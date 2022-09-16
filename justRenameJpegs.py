import os, shutil, sys

def crawl_dir_get_list(inpath):#recurse subfolders and get all file names
	filepath_list=[]
	for (path,dirs,files) in os.walk(inpath):
		for item in files:
			filepath=path+os.path.sep+item
			if filepath not in filepath_list:
				filepath_list.append(filepath)
	return sorted(filepath_list)

def rename(inpath):
    fileList = crawl_dir_get_list(inpath)
    for item in fileList:
    	if item.lower().endswith('.jpg'):
    		itemSplit = item.split()
    		itemSplitLength = len(itemSplit)
    		if itemSplitLength > 1:
    			newName = itemSplit[1]
    			if not newName.lower().endswith('.jpg'):
    				newName = newName+'.jpg'
    			target = inpath+'/'+newName
    			shutil.copyfile(item,target)

def argv_rename(inpath):
	#checks first argument from the command line
	if os.path.isdir(inpath):
		rename(inpath)

if __name__ == '__main__':
	if len(sys.argv)>=2:
		argv_rename(str(sys.argv[1]))#try to pass first argument to argv_rename
	else:
		print("Sample Usage: python justRenameJpegs.py /Users/path/to/jpegs")
