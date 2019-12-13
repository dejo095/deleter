import sys
from funcs import findUniqueDirs, printAllPaths, deleteAllPaths

while True:
  rootDir = input('Enter path where to scan for node_modules, eg. d:/foldername/ : ')

  if len(rootDir) < 1:
    print("Must enter root directory!")
  else:
    items = findUniqueDirs(rootDir)
    print(f'Node_modules will be deleted from following paths!: ')
    printAllPaths(items)
    confirm = input('Confirm deleting folders? (y)es/(n)o :')
    if confirm.lower() == 'y':
      deleteAllPaths(items)
    else:
      print('Ok, nothing was deleted! Bye!')
      sys.exit()

  if rootDir.lower is 'quit':
    print('Exiting, Bye!')
    sys.exit()