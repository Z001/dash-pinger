import urllib
import time
import datetime

def pinger_urllib(host):
  t1 = time.time()
  st = datetime.datetime.fromtimestamp(t1).strftime('%Y-%m-%d %H:%M:%S') + "   LOST CONNECTION"
  try:
    urllib.urlopen(host).read()
  except IOError:
    with open("test.txt", "a") as myfile:
      myfile.write("\n")
      myfile.write(st)
      return st
  else:
    return (time.time() - t1) * 1000.0
  

host = str(raw_input('host: '))

while True:
  print pinger_urllib(host)
  time.sleep(60)
  