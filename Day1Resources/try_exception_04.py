from urllib.request import urlopen
def isOnline(reliableserver="http://www.google.com"):
  try:
    urlopen(reliableserver)
    return True
  except IOError:
    return False
  
print(isOnline())
  
  
