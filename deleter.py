import sys
from funcs import findUniqueDirs, printAllPaths, deleteAllPaths

print("\nNode deleter - v.0.1 - by Dejo\nType \"quit\" to exit application!")

while True:

  rootDir = input('\nEnter path where to scan for node_modules, eg. d:/foldername/ : ')

  if rootDir == 'quit':
    print('Exiting, Bye!')
    break
  elif len(rootDir) < 6:
    print("Must enter root valid directory!")
  else:
    items = findUniqueDirs(rootDir)
    if len(items) != 0:
      print(f'Node_modules will be deleted from following paths!: ')
      printAllPaths(items)
      confirm = input('Confirm deleting folders? (y)es/(n)o :')

      if confirm.lower() != 'y':
        print(f'Ok, nothing was deleted from this {rootDir} path')
        # break
      else:
        deleteAllPaths(items)
    else:
      print(f"Nothing was found in the {rootDir} path!")
