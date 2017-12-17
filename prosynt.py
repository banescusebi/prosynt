#!/usr/bin/python
import sys
from capstone import *
import subprocess

def findEntryAndSize(path):
  readelfOutput = subprocess.Popen("readelf -t " + path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  found = False
  info = [None, None] # info[0] = entryPoint, info[1] = size
  index = 0
  for line in readelfOutput.stdout.readlines():
    if found:
      info[index] = line
      index += 1
    if line.find("text") > -1:
      found = True
    if index > 1:
      break;

  entryPoint = info[0].split()
  size = info[1].split()
  ep = int(entryPoint[3], 16)
  sz = int(size[0], 16)
  return (ep, sz)

# @path the location of the binary file
# Returns a byte buffer with the contents of the file
def readBinaryFile(path):
  contents = ""
  f = open(path, "rb")
  entryPoint, size = findEntryAndSize(path)
  f.read(entryPoint)
  try:
    byte = f.read(1)
    for i in range(size):
      contents += byte
      byte = f.read(1)
  finally:
    f.close()
  #print(contents)
  return contents

def printDisasm(path):
  try:
    code = readBinaryFile(path)
    #print(code)
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for i in md.disasm(code, 0x1000):
      print "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)

  except CsError as e:
    print("ERROR: %s" %e)

if __name__ == '__main__':
  printDisasm(sys.argv[1])
