import platform
import sys
import distro 

def linux_distribution():
  try:
    return distro.linux_distribution()
  except:
    return "Not Linux"

print("""Python version: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver()
))

#To completely understand zhis, go to http://thomas-cokelaer.info/tutorials/python/print.html#conversion-types 