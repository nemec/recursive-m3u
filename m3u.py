#!/usr/bin/python

import os
import sys
import re

usage = "m3u.py [options]\n-d <dir>\n-p <playlist-dir>\n-t <pipe-sep-filetypes>"

filetypes = "mp3|mp4"
musicDir = "/home/dan/snd/"
storageDir = musicDir+"playlists/"

for args in range(1,len(sys.argv)-1,2):
  arg = sys.argv[args]
  val = sys.argv[args+1]
  try:
    if arg == '-d':
      musicDir = val
    elif arg == '-p':
      storageDir = val
    elif arg == '-t':
      filetypes = val
    else:
      raise Exception
  except:
    print usage
    exit()

if musicDir[-1] != '/':
  musicDir = musicDir+'/'

if storageDir[-1] != '/':
  storageDir = storageDir+'/'

if not os.path.isdir(storageDir):
  os.mkdir(storageDir)

match = re.compile(".*\.("+filetypes+")$")

def listFiles(dr):
  dirs = os.listdir(dr)
  ret=[]
  for fil in dirs:
    path=os.path.join(dr,fil)
    if os.path.isdir(path):
      ret.extend(listFiles(path))
    if re.match(match, path):
      ret.append(path)
  return ret

# Get list of music dirs
dirs = os.listdir(musicDir)
for dr in dirs:
  name = dr[dr.rfind('/', 0, len(dr)-1)+1:]
  f = open(os.path.join(storageDir,name+".m3u"), "a")
  # Get list of files to write
  files = listFiles(os.path.join(musicDir,dr))
  for line in files:
    f.write(line+"\n")
  f.close()
  # Remove empty m3u, no music in dr
  if os.path.getsize(os.path.join(musicDir,dr)) == 0:
    os.remove(os.path.join(storageDir,name+".m3u"))
