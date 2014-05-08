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
      return "nahidi))"
  else:
    return (time.time() - t1) * 1000.0
  

host = str(raw_input('host: '))

while True:
  time.sleep(5)
  print pinger_urllib(host)