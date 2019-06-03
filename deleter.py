import sys
from funcs import findUniqueDirs, printAllPaths, deleteAllPaths

start_directory = input('Please enter folder from where to start removing node_modules folders and files, use full path: ')

if len(start_directory) < 1:
  print("Must enter start directory")
else:
  items = findUniqueDirs(start_directory)
  print(f'From these paths node_modules will be deleted:')
  printAllPaths(items)
  confirm = input('Are you sure you want to continue?: ')
  if confirm.lower() == 'y':
    deleteAllPaths(items)
  else:
    print('Ok, Bye!')
    sys.exit()
