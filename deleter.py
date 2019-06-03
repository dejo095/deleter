import sys
from funcs import findUniqueDirs, printAllPaths, deleteAllPaths

rootDir = input('Enter path from where to remove node_modules, use full path: ')

if len(rootDir) < 1:
  print("Must enter root directory!")
else:
  items = findUniqueDirs(rootDir)
  print(f'Node_modules will be deleted from following paths:')
  printAllPaths(items)
  confirm = input('Are you sure you want to continue with deleting?: ')
  if confirm.lower() == 'y':
    deleteAllPaths(items)
  else:
    print('Ok, nothing was deleted! Bye!')
    sys.exit()
