#!/usr/bin/python

import os
import sys

filetypes = "mp3;mp4"

# Create music dir or use default
musicDir = "/home/dan/snd/"
if len(sys.argv) == 2:
  musicDir = sys.argv[1]
if musicDir[-1] != '/':
  musicDir = musicDir+'/'
#Create m3u storage dir or use default
storageDir = musicDir+"playlists/"
if len(sys.argv) == 3:
  if sys.argv[2][0]=='/':
    storateDir = sys.argv[2]
  else:
    storageDir = os.path.join(musicDir,sys.argv[2])
if storageDir[-1] != '/':
  storageDir = storageDir+'/'
if not os.path.isdir(storageDir):
  os.mkdir(storageDir)

def listFiles(dr):
  dirs = os.listdir(dr)
  ret=[]
  for fil in dirs:
    if os.path.isdir(os.path.join(dr,fil)):
      ret.extend(listFiles(os.path.join(dr,fil)))
    ret.append(dr+fil)
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
