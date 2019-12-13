import os
import shutil

def findUniqueDirs(rootDir):

  delete_items = []

  for dirName, subdirList, fileList in os.walk(rootDir):
    # check only directories that have node_modules
    if (dirName.find('node_modules', 0, len(dirName)) != -1):
      # find at what char node_modules start
      pos = dirName.find("node_modules", 0, len(dirName))
      # extract from string whole path included node_modules
      path = dirName[:pos+12]
      # add path to list if path doesnt already exists
      if path not in delete_items:
        delete_items.append(path)
  return delete_items


def printAllPaths(items):
  for item in items:
    print(item)


def deleteAllPaths(listing):
  for item in listing:
    try:
      shutil.rmtree(item)
      print(f'Removed {item}')
    except OSError as e:
      print("Error: %s - %s." % (e.filename, e.strerror))