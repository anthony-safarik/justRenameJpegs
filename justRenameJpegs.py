import os
import sys


def rename(inpath):
    files = os.listdir(inpath)
    for f in files:
        fsplit = f.split()
        if f.lower().endswith('.jpg') and len(fsplit) > 1:
            shot = fsplit[1]
            old_path = os.path.join(inpath, f) 
            new_path = os.path.join(inpath,shot + '.jpg')
            os.rename(old_path,new_path)
            print(f'renamed... {shot}')

def argv_rename(inpath):
	#checks first argument from the command line
	if os.path.isdir(inpath):
		rename(inpath)

if __name__ == '__main__':
	if len(sys.argv)>=2:
		argv_rename(str(sys.argv[1]))#try to pass first argument to argv_rename
	else:
		# Uncomment and change paths to rename from fixed location(s) when no arg is used
		# argv_rename('/Users/stremland/Desktop/JPEGS')
		# argv_rename('/Users/streamland/Desktop/JPEGS')
		
        # Uncomment to rename from this file directory when no arg is used
        # abspath = os.path.abspath(__file__)
        # dirname = os.path.dirname(abspath)
		# argv_rename(dirname)
		
		print("Sample Usage: python justRenameJpegs.py /Users/path/to/jpegs")
