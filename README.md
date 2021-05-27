# justRenameJpegs
Removes gack from Jpeg file names. Used after exporting markers, using comments from Avid.

a stand-alone MacOS app has been built for this using py2app

$ pip install -U py2app

$ py2applet --make-setup MyApplication.py

edit the setup file:
APP = ['justRenameJpegs.py']

build the app in alias mode:
$ python setup.py py2app -A

Setup will make a build and dist folder. The app is in the dist folder. you can run the app from the command line if you open the contents:
dist/justRenameJpegs.app/Contents/MacOS/justRenameJpegs

remove build and dist folders:
$ rm -rf build dist

build the app for real:
$ python setup.py py2app
