import os
import sys
import shutil


start_directory = input('Please enter folder from where to start removing node_modules folders and files, use full path: ')
node_modules = "node_modules"
# os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir)

if len(start_directory) < 1:
  print("Must enter start directory") 
else:
  listing = os.listdir(start_directory) # list all files/folders in workdir
  for item in listing:
    if os.path.isdir(item) == True:
      os.chdir(item)
      if os.path.isdir(node_modules) == True:
        try:
          shutil.rmtree(node_modules)
          print(f'Removed {os.getcwd()}/node_modules ')
          os.chdir('..')
        except OSError as e:
          print("Error: %s - %s." % (e.filename, e.strerror))